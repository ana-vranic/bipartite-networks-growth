#!/bin/bash

python scripts/select_groups.py -r local ../reddit2017/reddit2017_groups > data_to2012year
python scripts/filter_small_groups.py -r local data_to2012year > data_to2012year_filtered

python scripts/number_of_new_users.py -r local data_to2012year_filtered > data_to2012year_newusers
python scripts/number_of_new_groups.py -r local data_to2012year_filtered > data_to2012year_newgroups
python scripts/number_of_active_users.py -r local data_to2012year_filtered > data_to2012year_activeusers

python scripts/calculate_delta_sizes.py -r local data_to2012year_filtered > data_to2012year_sizes
python scripts/calculate_rates.py -r local data_to2012year_sizes > data_to2012year_size_rate_lograte

python generate_ts.py




