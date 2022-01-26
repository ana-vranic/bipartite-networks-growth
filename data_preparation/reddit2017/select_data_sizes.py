import matplotlib.pyplot as plt
import math as mt
import json
import numpy as np
f = open('reddit2017/reddit2017_size_rate_lograte', 'r')

years_dict = {}
for line in f:
    year, data = line.split("\t")
    size = data.strip("[]\n").split(",")[1]
    curr = years_dict.get( year, [])
    curr.append(int(size))

    years_dict[year] = curr

f.close()

with open('reddit2017_sizes_per_year.json', 'w') as outfile:
    json.dump(years_dict, outfile)


years_dict_n = {}

for key in years_dict.keys():
    mean = np.mean(years_dict[key])
    data = [x/mean for x in years_dict[key] if x>0]
    years_dict_n[key] = data

with open('reddit2017_sizes_normed_per_year.json', 'w') as outfile:
    json.dump(years_dict_n, outfile)

