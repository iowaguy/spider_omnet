import sys
import argparse
import statistics as stat
from config import *

delay = 30

parser = argparse.ArgumentParser('Analysis Plots')
parser.add_argument('--topo',
        type=str, 
        required=True,
        help='what topology to generate size summary for')
parser.add_argument('--payment-graph-type',
        type=str, 
        help='what graph type topology to generate summary for', default="circ")
parser.add_argument('--credit',
        type=int,
        help='Credit to collect stats for', default=10)
parser.add_argument('--demand',
        type=int,
        help='Single number denoting the demand to collect data for', default="30")
parser.add_argument('--path-type-list',
        nargs="*",
        help='types of paths to collect data for', default=["shortest"])
parser.add_argument('--scheme-list',
        nargs="*",
        help='set of schemes to aggregate results for', default=["priceSchemeWindow"])
parser.add_argument('--save',
        type=str, 
        required=True,
        help='file name to save data in')
parser.add_argument('--num-max',
        type=int,
        help='Single number denoting the maximum number of runs to aggregate data over', default="5")

# collect all arguments
args = parser.parse_args()
topo = args.topo
credit_list = args.credit_list
demand = args.demand
path_type_list = args.path_type_list
scheme_list = args.scheme_list





output_file = open(PLOT_DIR + args.save, "w+")
output_file.write("Scheme,Credit,SuccVol,Demand\n")


# go through all relevant files and aggregate probability by size
for credit in credit_list:
    for scheme in scheme_list:
        for path_type in path_type_list:
            succ_volume_list = []
            for run_num in range(1, args.num_max + 1):
                file_name = topo + "_" + args.payment_graph_type + "_" + str(credit) + "_" + scheme + "_" + \
                        args.payment_graph_type + str(run_num) + \
                    "_demand" + str(demand/10) + "_" + path_type
                if scheme != "shortestPath":
                    filename += "_" + str(num_paths)
                filename += "-#0.sca"
               
               # num_completed will always be populated first and the next
               # entry will be arrived for the same flow
               # based on file structure
                with open(SUMMARY_DIR + file_name) as f:
                    for line in f:
                        if "->" in line:
                            if "amtCompleted" in line:
                                parts = shlex.split(line)
                                num_completed = float(parts[-1])
                            if "amtArrived" in line:
                                parts = shlex.split(line)
                                num_arrived = float(parts[-1])
                                flow_succ_list.append(num_completed/num_arrived)

            for entry in sorted(flow_succ_list):
                output_file.write(str(SCHEME_CODE[scheme]) +  "," + str(credit) +  "," + \
                    "%f,%f\n" % (entry, demand))
output_file.close()