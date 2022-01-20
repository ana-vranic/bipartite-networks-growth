#!/bin/bash
#PBS -q standard
#PBS -l nodes=1:ppn=4
#PBS -e ${PBS_JOBID}.err
#PBS -o ${PBS_JOBID}.out


source juliaenv.sh
cd ${PBS_O_WORKDIR}
export JULIA_NUM_THREADS=4

julia codes/run.jl ${p_active} ${p_gf} ${p_gj} ${p_sample} ${random_linking} ${input_file} ${output_file} ${nsamples}

mkdir -p "results_sizes/${net}"


folder="results/${net}/pactive${p_active}_pnewgroup${p_gf}_paff${p_gj}"

input_file="${folder}/${net}_pactive${p_active}_pnewgroup${p_gf}_paff${p_gj}_psample${p_sample}_${random_linking}"

output_file_s="results_sizes/${net}/sizes_${net}_pactive${p_active}_pnewgroup${p_gf}_paff${p_gj}_psample${p_sample}_${random_linking}.txt"

output_file_r="results_sizes/${net}/rates_${net}_pactive${p_active}_pnewgroup${p_gf}_paff${p_gj}_psample${p_sample}_${random_linking}.txt"

output_file_lr="results_sizes/${net}/logrates_${net}_pactive${p_active}_pnewgroup${p_gf}_paff${p_gj}_psample${p_sample}_${random_linking}.txt"

julia codes/calculate_sizes_sample.jl ${input_file} ${output_file_s} ${nsamples}
julia codes/calculate_rates_sample.jl ${input_file} ${output_file_r} ${output_file_lr} ${nsamples}

