import matplotlib.pyplot as plt
import numpy as np
import math as mt
import json
f = open('reddit2017/reddit2017_size_rate_lograte', 'r')
years_dict = {}
for line in f:
    subreddit, data = line.split("\t")
    year = subreddit.strip("[]\n").split(",")[1]
    size = data.strip("[]\n").split(",")[0]
    rate = data.strip("[]\n").split(",")[1]
    lograte = data.strip("[]\n").split(",")[2]
    curr = years_dict.get(int(year), [])
    curr.append(float(lograte))
    years_dict[int(year)] = curr   
f.close()

with open('reddit2017_logrates_per_year.json', 'w') as outfile:
    json.dump(years_dict, outfile)

years_dict_n = {}

for key in years_dict.keys():
    mean = np.mean(years_dict[key])
    data = [x/mean for x in years_dict[key] if x>0]
    years_dict_n[key] = data

with open('reddit2017_logrates_normed_per_year.json', 'w') as outfile:
    json.dump(years_dict_n, outfile)



