#!/bin/bash
#PBS -q standard
#PBS -l nodes=1:ppn=16
#PBS -e ${PBS_JOBID}.err
#PBS -o ${PBS_JOBID}.out


source juliaenv.sh
cd ${PBS_O_WORKDIR}
export JULIA_NUM_THREADS=16

julia codes/run.jl ${pa} ${pg} ${paff} ${random_linking} ${input_file} ${output_file} ${nsamples}

mkdir -p "results_sizes/${net}"

folder="results/${net}/pactive${pa}_pnewgroup${pg}_paff${paff}"

input_file="${folder}/${net}_pactive${pa}_pnewgroup${pg}_paff${paff}_${random_linking}"

output_file_s="results_sizes/${net}/sizes_${net}_pactive${pa}_pnewgroup${pg}_paff${paff}_${random_linking}.txt"

output_file_r="results_sizes/${net}/rates_${net}_pactive${pa}_pnewgroup${pg}_paff${paff}_${random_linking}.txt"

output_file_lr="results_sizes/${net}/logrates_${net}_pactive${pa}_pnewgroup${pg}_paff${paff}_${random_linking}.txt"

julia codes/calculate_sizes_sample.jl ${input_file} ${output_file_s} ${nsamples}
julia codes/calculate_rates_sample.jl ${input_file} ${output_file_r} ${output_file_lr} ${nsamples}

