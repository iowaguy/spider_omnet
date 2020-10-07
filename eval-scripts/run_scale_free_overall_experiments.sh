#!/bin/bash
# NOTE: while a single OMNET experiment uses a single core,
# the memory consumption of each one of these runs can be on the order o
# 50 GB for a scale free run
# this script assumes you can run the schemes - DCTCP and waterfilling
# in parallel, but precisely one
# experiment per scheme
# (in total there are 5 balances * 5 circulations = 25 experiments per scheme)
# Do not use this script as is, without first judging the capabilities of
# your system to run experiments in parallel

# Scale free topology, kaggle data for transactions

# LND balances, remove "analyze-only" flag to run experiments
# make sure widest paths are generated
# Figures 9-10 of https://people.csail.mit.edu/vibhaa/files/spider_nsdi.pdf
for scheme in "DCTCPQ" "waterfilling" "lndBaseline" "landmarkRouting" "shortestPath"
do
    ./run_experiment_set.sh \
        --prefix=sf_50_routers_lndCap \
        --workload-prefix=sf_50_routers \
        --exp-type=circ \
        --routing-scheme=${scheme} \
        --num-start=0 --num-end=4 \
        --balance-list="900 1350 2750 4000 8750" \
        --path-choice=widest \
        --num-paths=4 \
        --demand-scale="3" \
	--scheduling-alg=LIFO &
#        --analyze-only &
done
wait

# uniform balances, remove "analyze-only" flag to run experiments
# Figures 22-23 of https://people.csail.mit.edu/vibhaa/files/spider_nsdi.pdf
for scheme in "DCTCPQ" "waterfilling" "lndBaseline" "landmarkRouting" "shortestPath"
do
    ./run_experiment_set.sh \
        --prefix=sf_50_routers \
        --workload-prefix=sf_50_routers \
        --exp-type=circ \
        --routing-scheme=${scheme} \
        --num-start=0 --num-end=4 \
        --balance-list="100 200 400 800 1600 3200" \
        --path-choice=shortest \
        --num-paths=4 \
        --demand-scale="3" \
	--scheduling-alg=LIFO &
#        --analyze-only &
done
wait
