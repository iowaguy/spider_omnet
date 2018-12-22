import sys
import textwrap
import argparse
import networkx as nx
from config import *
import re


def parseNodeName(nodeName, max_router, max_host):
    try:
        val = int(nodeName[:-1])
        if(nodeName[-1] == 'r'):
            if(val > max_router):
                max_router = val
            return ("router[" + str(val) + "]", max_router, max_host)
        if(nodeName[-1] == 'e'):
            if(val > max_host):
                max_host = val
            return ("host[" + str(val) + "]", max_router, max_host)
        return -1
    except:
        return -1



# take the topology file in a specific format and write it to a ned file
def write_ned_file(topo_filename, output_filename, network_name):
    # topo_filename must be a text file where each line contains the ids of two neighbouring nodes that 
    # have a payment channel between them, relative delays in each direction,  initial balance on each 
    # end (see sample-topology.txt)
    # each line is of form:
    # [node1] [node2] [1->2 delay] [2->1 delay] [balance @ 1] [balance @ 2]
    topo_file = open(topo_filename).readlines() 
    outfile = open(output_filename, "w")

    # metadata used for forwarding table
    neighbor_interfaces = dict()
    node_interface_count = dict()
    node_used_interface = dict()
    linklist = list()
    max_val = -1 #used to find number of nodes, assume nodes start at 0 and number consecutively
    max_router = -1
    max_host = -1
    for line in topo_file:
        if line == "\n":
            continue

        n1 = parseNodeName(line.split()[0], max_router, max_host)
        if(n1 == -1):
            print "Bad line " + line
            continue
        max_router = n1[1]
        max_host = n1[2]

        n2 = parseNodeName(line.split()[1], max_router, max_host)
        if(n2 == -1):
            print "Bad line " + line
            continue
        max_router = n2[1]
        max_host = n2[2]

        n3 = float(line.split()[2]) # delay going from n1 to n2
        n4 = float(line.split()[3]) # delay going from n2 to n1

        linklist.append((n1[0], n2[0], n3, n4))

    max_router = max_router + 1
    max_host = max_host + 1

    # generic routerNode and hostNode definition that every network will have
    outfile.write("import routerNode;\n")
    outfile.write("import hostNode;\n\n")

    outfile.write("network " + network_name + "\n")
    outfile.write("{\n")

    # This script (meant for a simpler datacenter topology) just assigns the same link delay to all links.
    # You need to change this such that the parameter values are instead assigned on a per node basis and 
    # are read from an additional 'delay' column and 'channel balance' columns in the text file.
    outfile.write('\tparameters:\n\t\tdouble linkDelay @unit("s") = default(100us);\n')
    outfile.write('\t\tdouble linkDataRate @unit("Gbps") = default(1Gbps);\n')
    outfile.write('\tsubmodules:\n')
    outfile.write('\t\thost['+str(max_host)+']: hostNode {} \n')
    outfile.write('\t\trouter['+str(max_router)+']: routerNode {} \n')
    outfile.write('connections: \n')

    for link in linklist:
        a = link[0]
        b = link[1]
        abDelay = link[2]
        baDelay = link[3]

        outfile.write('\t\t' + a + '.out++ --> {delay = ' + str(abDelay) +'ms; }')
        outfile.write(' --> ' + b + '.in++;  \n')
        outfile.write('\t\t' + a + '.in++ <-- {delay = ' + str(baDelay) +'ms; }')
        outfile.write(' <-- ' + b + '.out++;  \n')
    outfile.write('}\n')




# generate either a small world or scale free graph
def generate_graph(size, graph_type):
    if graph_type == 'small_world':
        G = nx.watts_strogatz_graph(size, size/8, 0.25, seed=SEED)
    elif graph_type == 'scale_free':
        G = nx.scale_free_graph(size,seed=SEED)

    # remove self loops and parallel edges
    G.remove_edges_from(G.selfloop_edges())
    G = nx.Graph(G)

    print 'Generated a ', graph_type, ' graph'
    print 'number of nodes: ', G.number_of_nodes()
    print 'Number of Edges: ', G.number_of_edges()
    return G




# print the output in the desired format for write_ned_file to read
# generate extra end host nodes if need be
def print_topology_in_format(G, balance_per_channel, delay_per_channel, output_filename, separate_end_hosts):
    f1 = open(output_filename, "w+")
    f2 = open("for_workload_" + output_filename, "w+")

    offset = G.number_of_nodes()
    if (separate_end_hosts == False):
        offset = 0

    for e in G.edges():

        f1.write(str(e[0]) + "r " + str(e[1]) +  "r ")
        f1.write(str(delay_per_channel) + " " + str(delay_per_channel) + " ")
        f1.write(str(balance_per_channel/2) + " " + str(balance_per_channel/2) + "\n")
        f2.write(str(e[0] + offset) + "r " + str(e[1] + offset) +  "r ")
        f2.write(str(delay_per_channel) + " " + str(delay_per_channel) + " ")
        f2.write(str(balance_per_channel/2) + " " + str(balance_per_channel/2) + "\n")


    # generate extra end host nodes
    if separate_end_hosts: 
        f2.write("\n")
        for n in G.nodes():
            f1.write(str(n) + "e " + str(n) + "r ")
            f1.write(str(delay_per_channel) + " " + str(delay_per_channel) + " ")
            f1.write(str(0) + " " + str(LARGE_BALANCE) + "\n")
            f2.write(str(n) + "e " + str(n + offset) + "r ")
            f2.write(str(delay_per_channel) + " " + str(delay_per_channel) + " ")
            f2.write(str(0) + " " + str(LARGE_BALANCE) + "\n")
    f1.close()
    f2.close()




# parse arguments
parser = argparse.ArgumentParser(description="Create arbitrary topologies to run the omnet simulator on")
parser.add_argument('--num-nodes', type=int, dest='num_nodes', help='number of nodes in the graph', default=20)
parser.add_argument('--delay-per-channel', type=int, dest='delay_per_channel', \
        help='delay between nodes (ms)', default=30)
parser.add_argument('graph_type', choices=['small_world', 'scale_free', 'hotnets_topo', 'simple_line', \
        'simple_deadlock'], \
        help='type of graph (Small world or scale free or custom topology list)', default='small_world')
parser.add_argument('--balance-per-channel', type=int, dest='balance_per_channel', default=100)
parser.add_argument('--topo-filename', dest='topo_filename', type=str, \
        help='name of intermediate output file', default="topo.txt")
parser.add_argument('--network-name', type=str, dest='network_name', \
        help='name of the output ned filename', default='simpleNet')
parser.add_argument('--separate-end-hosts', action='store_true', \
        help='do you need separate end hosts that only send transactions')

args = parser.parse_args()


# generate graph and print topology and ned file
if args.graph_type in ['small_world', 'scale_free']:
    G = generate_graph(args.num_nodes, args.graph_type)
elif args.graph_type == 'hotnets_topo':
    G = hotnets_topo_graph
elif args.graph_type == 'simple_deadlock':
    G = simple_deadlock_graph
    args.separate_end_hosts = False
else:
    G = simple_line_graph
    args.separate_end_hosts = False


print_topology_in_format(G, args.balance_per_channel, args.delay_per_channel, args.topo_filename, \
        args.separate_end_hosts)
write_ned_file(args.topo_filename, args.network_name + '.ned', args.network_name)


