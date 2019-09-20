#!/bin/bash

pipenv install

declare -a LEARNING_RATE_LIST=('0.0001' '0.001' '0.0005')
declare -a ITERATIONS_LIST=('100' '1000' '5000' '7000' '10000')

for RATE in "${LEARNING_RATE_LIST[@]}"
do
    export LEARNING_RATE=$RATE
    for ITER in "${ITERATIONS_LIST[@]}"
    do
        echo "Running for LEARNING_RATE: $RATE and ITERATIONS: $ITER"
        mkdir figures/"${RATE}_${ITER}"
        export ITERATIONS=$ITER
        pipenv run training
    done
done