#!/bin/bash
net="N30"
input_file="new_users_${net}.txt"
for random_linking in  "random"
do
for p_active in 0.1
do
    for p_gf in 0.005
    do
        for p_gj in 0.8
        do 
           for p_sample in 0.1
              do
            folder="results/${net}/pactive${p_active}_pnewgroup${p_gf}_paff${p_gj}"
            mkdir -p ${folder}
            output_file="${folder}/${net}_pactive${p_active}_pnewgroup${p_gf}_paff${p_gj}_psample${p_sample}_${random_linking}"
            julia run.jl ${p_active} ${p_gf} ${p_gj} ${p_sample} ${random_linking} ${input_file} ${output_file}
        done
   done
done
done
done
