#!/bin/bash
#PBS -q standard
#PBS -l nodes=1:ppn=16
#PBS -e ${PBS_JOBID}.err
#PBS -o ${PBS_JOBID}.out

cd ${PBS_O_WORKDIR}
module load python/3.6.5
source ../mrjob_test/.venv/bin/activate


for year in "2017"
do
loc="reddit${year}/"
mkdir -p ${loc}
python 01-select_groups_by_year.py -r local ../first_post --maxYear ${year} > ${loc}/reddit${year}_groups
python 02-calulate-delta_size.py -r local ${loc}/reddit${year}_groups > ${loc}/reddit${year}_delta_sizes
python 03-calulate-rates.py -r local ${loc}/reddit${year}_delta_sizes > ${loc}/reddit${year}_size_rate_lograte

#python filter_small_groups.py -r local data_to2012year > data_to2012year_filtered
done


