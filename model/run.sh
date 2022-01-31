#!/bin/bash
net="cityNY"
input_file="new_users_${net}.txt"

nsamples=1
random_linking="random"  #"preferential"

pa=0.05
pg=0.003
paff=0.8

folder="results/${net}/pactive${pa}_pnewgroup${pg}_paff${paff}"
mkdir -p ${folder}

output_file="${folder}/${net}_pactive${pa}_pnewgroup${pg}_paff${paff}_${random_linking}"

qsub -v net=${net},nsamples=${nsamples},pa=${pa},pg=${pg},paff=${paff},random_linking=${random_linking},input_file=${input_file},output_file=${output_file} submit.sh
