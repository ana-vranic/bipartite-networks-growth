#!/bin/bash
net="N30"
input_file="new_users_${net}.txt"
nsamples=100
for random_linking in "random" "preferential"
do
for p_active in 0.1 0.5 0.8
do
    for p_gf in 0.1 0.5 0.8
    do
        for p_gj in 0.0
        do 
           for p_sample in 1.0
              do
            folder="results/${net}/pactive${p_active}_pnewgroup${p_gf}_paff${p_gj}"
            mkdir -p ${folder}
            output_file="${folder}/${net}_pactive${p_active}_pnewgroup${p_gf}_paff${p_gj}_psample${p_sample}_${random_linking}"
            qsub -v net=${net},nsamples=${nsamples},p_active=${p_active},p_gf=${p_gf},p_gj=${p_gj},p_sample=${p_sample},random_linking=${random_linking},input_file=${input_file},output_file=${output_file} submit1.sh
              done
        done
    done
done
done

