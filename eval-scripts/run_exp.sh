#!/bin/bash
PATH_NAME="$HOME/$OMNET/samples/spider_omnet/benchmarks/circulations/"
GRAPH_PATH="$HOME/$OMNET/samples/spider_omnet/scripts/figures/"

num_nodes=("2" "2" "3" "4" "5" "5" "5" "0" "0" "10" "20" "50" "60" "80" "100" "200" "400" "600" "800" "1000" \
    "10" "20" "50" "60" "80" "100" "200" "400" "600" "800" "1000" "40" "10" "20" "30" "40" "0" "0" "11" "4")

#balance=100

prefix=(
  "two_node_imbalance"     #0
  "two_node_capacity"      #1
  "three_node"             #2
  "four_node"              #3
  "five_node_hardcoded"    #4
  "hotnets"                #5
  "five_line"              #6
  "lnd_dec4_2018"          #7
  "lnd_dec4_2018lessScale" #8
  "sw_10_routers"          #9
  "sw_20_routers"          #10
  "sw_50_routers"          #11
  "sw_60_routers"          #12
  "sw_80_routers"          #13
  "sw_100_routers"         #14
  "sw_200_routers"         #15
  "sw_400_routers"         #16
  "sw_600_routers"         #17
  "sw_800_routers"         #18
  "sw_1000_routers"        #19
  "sf_10_routers"          #20
  "sf_20_routers"          #21
  "sf_50_routers"          #22
  "sf_60_routers"          #23
  "sf_80_routers"          #24
  "sf_100_routers"         #25
  "sf_200_routers"         #26
  "sf_400_routers"         #27
  "sf_600_routers"         #28
  "sf_800_routers"         #29
  "sf_1000_routers"        #30
  "tree_40_routers"        #31
  "random_10_routers"      #32
  "random_20_routers"      #33
  "random_30_routers"      #34
  "sw_sparse_40_routers"   #35
  "lnd_gaussian"           #36
  "lnd_uniform"            #37
  "toy_dctcp"              #38
  "parallel_graph"         #39
)


demand_scale=("10") # "60" "90")
routing_scheme=$1
pathChoice=$2
schedulingAlgorithm=$3
echo $routing_scheme
random_init_bal=false
random_capacity=false

widestPathsEnabled=false
obliviousRoutingEnabled=false
kspYenEnabled=false

#general parameters that do not affect config names
simulationLength=1000
statCollectionRate=5
timeoutClearRate=1
timeoutEnabled=true
signalsEnabled=true
loggingEnabled=false
transStatStart=0
transStatEnd=2000
mtu=1.0

# scheme specific parameters
eta=0.025
alpha=0.2
kappa=0.025
updateQueryTime=1.5
minPriceRate=0.25
zeta=0.01
rho=2
tau=10
normalizer=100
xi=1
routerQueueDrainTime=5
serviceArrivalWindow=300

#DCTCP parameters
windowBeta=0.1
windowAlpha=0.5
queueThreshold=20
queueDelayThreshold=300
balanceThreshold=0.01
minDCTCPWindow=1
rateDecreaseFrequency=3.0

for suffix in "Base" "Waterfilling" "LndBaseline" "PriceScheme" "DCTCP" "Celer"
do
    cp hostNode${suffix}.ned ${PATH_NAME}
    cp routerNode${suffix}.ned ${PATH_NAME}
done
cp hostNodeLandmarkRouting.ned ${PATH_NAME}
cp routerNodeDCTCPBal.ned ${PATH_NAME}
cp hostNodePropFairPriceScheme.ned ${PATH_NAME}


arraylength=${#prefix[@]}
PYTHON="$(which python)"
mkdir -p ${PATH_NAME}

if [ -z "$pathChoice" ]; then
    pathChoice="shortest"
fi

if [ -z "$schedulingAlgorithm" ]; then
    schedulingAlgorithm="LIFO"
fi

echo $pathChoice
echo $schedulingAlgorithm

echo "${#num_nodes[@]}"


# TODO: find the indices in prefix of the topologies you want to run on and then specify them in array
# adjust experiment time as needed
#array=( 0 1 4 5 8 19 32)
array=( 22 ) #10 11 13 22 24)
for i in "${array[@]}"
do
    for balance in 100 #200 300 600 900 #2000 9000
    do
        echo ${prefix[i]}
        network="${prefix[i]}_circ_net"
        topofile="${PATH_NAME}${prefix[i]}_topo${balance}.txt"

        # identify graph type for topology
        if [ ${prefix[i]:0:2} == "sw" ]; then
            graph_type="small_world"
        elif [ ${prefix[i]:0:2} == "sf" ]; then
            graph_type="scale_free"
        elif [ ${prefix[i]:0:4} == "tree" ]; then
            graph_type="tree"
        elif [ ${prefix[i]:0:3} == "lnd" ]; then
            graph_type=${prefix[i]}
        elif [ ${prefix[i]} == "hotnets" ]; then
            graph_type="hotnets_topo"
        elif [ ${prefix[i]} == "toy_dctcp" ]; then
            graph_type="toy_dctcp"
        elif [ ${prefix[i]:0:8} == "parallel" ]; then
            graph_type="parallel_graph"
        elif [ ${prefix[i]:0:6} == "random" ]; then
            graph_type="random"
        else
            graph_type="simple_topologies"
        fi

        # set delay amount
        if [[ (${prefix[i]:0:3} == "two") || (${prefix[i]:0:5} == "three") ]]; then
            delay="120"
        else
            delay="30"
        fi

        # STEP 1: create topology
        $PYTHON scripts/create_topo_ned_file.py $graph_type\
                --network-name ${PATH_NAME}$network\
                --topo-filename $topofile\
                --num-nodes ${num_nodes[i]}\
                --balance-per-channel $balance\
                --separate-end-hosts \
                --delay-per-channel $delay\
                --randomize-start-bal $random_init_bal\
                --random-channel-capacity $random_capacity


        # create workload files and run different demand levels
        for scale in "${demand_scale[@]}"
        do

            # generate the graph first to ned file
            workloadname="${prefix[i]}_circ_demand${scale}"
            workload="${PATH_NAME}$workloadname"
            inifile="${PATH_NAME}${workloadname}_default.ini"
            payment_graph_topo="custom"

            # figure out payment graph/workload topology
            if [ ${prefix[i]:0:9} == "five_line" ]; then
                payment_graph_topo="simple_line"
            elif [ ${prefix[i]:0:5} == "three" ]; then
                payment_graph_topo="simple_line"
            elif [ ${prefix[i]:0:4} == "five" ]; then
                payment_graph_topo="hardcoded_circ"
            elif [ ${prefix[i]:0:3} == "toy" ]; then
                payment_graph_topo="toy_dctcp"
            elif [ ${prefix[i]:0:7} == "hotnets" ]; then
                payment_graph_topo="hotnets_topo"
            elif [ ${prefix[i]:0:8} == "parallel" ]; then
                payment_graph_topo="parallel_graph"
            fi

            echo $network
            echo $topofile
            echo $inifile
            echo $graph_type

            # STEP 1: create transactions corresponding to this experiment run
            $PYTHON scripts/create_workload.py $workload poisson \
                    --graph-topo $payment_graph_topo \
                    --payment-graph-dag-percentage 0\
                    --topo-filename $topofile\
                    --experiment-time $simulationLength \
                    --balance-list $balance\
                    --generate-json-also \
                    --timeout-value 5 \
                    --scale-amount $scale \
                    --run-num 0

            # STEP 3: run the experiment
            # routing schemes where number of path choices doesn't matter
            if [ "${routing_scheme}" ==  "shortestPath" ]; then
              output_file=outputs/${prefix[i]}_${balance}_circ_${routing_scheme}_demand${scale}0_${pathChoice}
              inifile=${PATH_NAME}${prefix[i]}_${balance}_circ_${routing_scheme}_demand${scale}_${pathChoice}.ini

              # create the ini file with specified parameters
              python scripts/create_ini_file.py \
                      --network-name ${network}\
                      --topo-filename ${topofile}\
                      --workload-filename ${workload}_workload.txt\
                      --ini-filename $inifile\
                      --signals-enabled $signalsEnabled\
                      --logging-enabled $loggingEnabled\
                      --simulation-length $simulationLength\
                      --stat-collection-rate $statCollectionRate\
                      --timeout-clear-rate $timeoutClearRate\
                      --timeout-enabled $timeoutEnabled\
                      --routing-scheme ${routing_scheme}\
                      --demand-scale ${scale}\
                      --transStatStart $transStatStart\
                      --transStatEnd $transStatEnd\
                      --path-choice $pathChoice\
                      --balance $balance


              # run the omnetexecutable with the right parameters
              ./spiderNet -u Cmdenv -f $inifile -c ${network}_${balance}_${routing_scheme}_demand${scale}_${pathChoice}_${schedulingAlgorithm} -n ${PATH_NAME}\
                    > ${output_file}.txt &

          else
              pids=""
              # if you add more choices for the number of paths you might run out of cores/memory
              for numPathChoices in 4
              do
                output_file=outputs/${prefix[i]}_${balance}_circ_${routing_scheme}_demand${scale}0_${pathChoice}_${numPathChoices}
                inifile=${PATH_NAME}${prefix[i]}_${balance}_circ_${routing_scheme}_demand${scale}_
		inifile=${inifile}${pathChoice}_${numPathChoices}.ini

                if [[ $routing_scheme =~ .*Window.* ]]; then
                    windowEnabled=true
                else
                    windowEnabled=false
                fi


                echo "Creating ini file"
                # create the ini file with specified parameters
                python scripts/create_ini_file.py \
                        --network-name ${network}\
                        --topo-filename ${topofile}\
                        --workload-filename ${workload}_workload.txt\
                        --ini-filename ${inifile}\
                        --signals-enabled $signalsEnabled\
                        --logging-enabled $loggingEnabled\
                        --simulation-length $simulationLength\
                        --stat-collection-rate $statCollectionRate\
                        --timeout-clear-rate $timeoutClearRate\
                        --timeout-enabled $timeoutEnabled\
                        --routing-scheme ${routing_scheme}\
                        --num-path-choices ${numPathChoices}\
                        --zeta $zeta\
                        --alpha $alpha\
                        --eta $eta\
                        --kappa $kappa\
                        --rho $rho\
                        --update-query-time $updateQueryTime\
                        --min-rate $minPriceRate\
                        --tau $tau\
                        --normalizer $normalizer \
                        --window-enabled $windowEnabled\
                        --demand-scale $scale\
                        --xi $xi\
                        --router-queue-drain-time $routerQueueDrainTime\
                        --service-arrival-window $serviceArrivalWindow\
                        --transStatStart $transStatStart\
                        --transStatEnd $transStatEnd\
                        --path-choice $pathChoice\
                        --balance $balance \
                        --window-alpha $windowAlpha \
                        --window-beta $windowBeta \
                        --queue-threshold $queueThreshold \
                        --scheduling-algorithm $schedulingAlgorithm\
                        --queue-delay-threshold $queueDelayThreshold \
                        --balance-ecn-threshold $balanceThreshold \
                        --mtu $mtu\
                        --min-dctcp-window $minDCTCPWindow \
                        --rate-decrease-frequency $rateDecreaseFrequency


                # run the omnetexecutable with the right parameters
                # in the background
                ./spiderNet -u Cmdenv -f ${inifile}\
                    -c ${network}_${balance}_${routing_scheme}_demand${scale}_${pathChoice}_${numPathChoices}_${schedulingAlgorithm}  -n ${PATH_NAME}\
                    > ${output_file}.txt &
                pids+=($!)
                done
            fi
            wait # for all algorithms to complete for this demand

            # STEP 4: plot everything for this demand
            # TODO: add plotting script
            echo "Plotting"
            payment_graph_type='circ'
            if [ "$timeoutEnabled" = true ] ; then timeout=""; else timeout="no_timeouts"; fi
            if [ "$random_init_bal" = true ] ; then suffix="randomInitBal_"; else suffix=""; fi
            if [ "$random_capacity" = true ]; then suffix="${suffix}randomCapacity_"; fi
            echo $suffix
            graph_op_prefix=${GRAPH_PATH}${timeout}/${prefix[i]}${balance}_delay${delay}_demand${scale}0_${suffix}
            vec_file_prefix=${PATH_NAME}results/${prefix[i]}_${payment_graph_type}_net_${balance}_

            #routing schemes where number of path choices doesn't matter
            if [ "${routing_scheme}" ==  "shortestPath" ]; then
                vec_file_path=${vec_file_prefix}${routing_scheme}_demand${scale}_${pathChoice}_${schedulingAlgorithm}-#0.vec
                sca_file_path=${vec_file_prefix}${routing_scheme}_demand${scale}_${pathChoice}_${schedulingAlgorithm}-#0.sca


                python scripts/generate_analysis_plots_for_single_run.py \
                  --detail $signalsEnabled \
                  --vec_file ${vec_file_path} \
                  --sca_file ${sca_file_path} \
                  --save ${graph_op_prefix}${routing_scheme}_${pathChoice} \
                  --balance \
                  --queue_info --timeouts --frac_completed \
                  --inflight --timeouts_sender \
                  --waiting --bottlenecks --time_inflight


            #routing schemes where number of path choices matter
            else
              for numPathChoices in 4
                do
                    vec_file_path=${vec_file_prefix}${routing_scheme}_demand${scale}_${pathChoice}_${numPathChoices}_${schedulingAlgorithm}-#0.vec
                    sca_file_path=${vec_file_prefix}${routing_scheme}_demand${scale}_${pathChoice}_${numPathChoices}_${schedulingAlgorithm}-#0.sca


                    python scripts/generate_analysis_plots_for_single_run.py \
                      --detail $signalsEnabled \
                      --vec_file ${vec_file_path} \
                      --sca_file ${sca_file_path} \
                      --save ${graph_op_prefix}${routing_scheme}_${pathChoice}_${numPathChoices} \
                      --balance \
                      --queue_info --timeouts --frac_completed \
                      --frac_completed_window \
                      --inflight --timeouts_sender --time_inflight \
                      --waiting --bottlenecks --probabilities \
                      --mu_local --lambda --n_local --service_arrival_ratio --inflight_outgoing \
                      --inflight_incoming --rate_to_send --price --mu_remote --demand \
                      --rate_sent --amt_inflight_per_path --rate_acked --fraction_marked --queue_delay \
                      --cpi --perDestQueue --kStar
                  done
              fi

            # STEP 5: cleanup
            #rm ${PATH_NAME}${prefix[i]}_circ*_demand${scale}.ini
            #rm ${workload}_workload.txt
            #rm ${workload}.json
        done
        #rm $topofile
    done
done
