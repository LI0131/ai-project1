#!/bin/bash

pipenv install

declare -a DB_ROWS=( 'crime_rate' 'zoned_over_25000' 'business_acres' 'river_var' 'nitric_oxide' \
    'rooms_per_home' 'built_prior_1940' 'distance_to_centers' 'highway_availability' \
    'property_tax' 'student_teacher_ratio' 'ethicity_demo' 'percent_lower_status' \
    'median_home_value')
declare -a LEARNING_RATE_LIST=('0.0019' '0.0019' '0.0019' '0.001' '0.001' '0.0019' '0.0019' '0.0019' '0.0019' '0.00192' '0.0019' '0.0018' '0.0019' '0.001')
declare -a ITERATIONS_LIST=('10000' '10000' '10000' '1000' '1000' '10000' '9000' '5000' '10000' '10000' '10000' '10000' '10000' '200')

for ((i=0;i<${#DB_ROWS[@]};++i));
do
    export LEARNING_RATE=${LEARNING_RATE_LIST[i]}
    export FEATURE=${DB_ROWS[i]}
    export ITERATIONS=${ITERATIONS_LIST[i]}
    echo "Running for DB_ROW: ${DB_ROWS[i]} LEARNING_RATE: ${LEARNING_RATE_LIST[i]} and ITERATIONS: ${ITERATIONS_LIST[i]}"
    rm -rf figures/"${DB_ROWS[i]}_${LEARNING_RATE_LIST[i]}_${ITERATIONS_LIST[i]}"
    mkdir figures/"${DB_ROWS[i]}_${LEARNING_RATE_LIST[i]}_${ITERATIONS_LIST[i]}"
    pipenv run training
done

unset FEATURE
unset LEARNING_RATE
unset ITERATIONS