import matplotlib.pyplot as plt
import numpy as np
import math as mt
import json
f = open('data_to2012_size_rate_lograte', 'r')
data_sizes = []
data_logrates = []
data_size_rate = []

for line in f:
    subreddit, data = line.split("\t")
    year = subreddit.strip("[]\n").split(",")[1]
    size = data.strip("[]\n").split(",")[0]
    rate = data.strip("[]\n").split(",")[1]
    lograte = data.strip("[]\n").split(",")[2]
    data_sizes.append(size)
    data_logrates.append(lograte)
    data_size_rate.append((size, lograte))
f.close()

np.savetxt(data_sizes, "data2012_sizes.txt")
np.savetxt(data_logrates, "data2012_logrates.txt")
np.savetxt(data_size_rate, "data2012_sizes_rates.txt")


#mean = np.mean(data)
#data = [x/mean for x in data if x>0]

#np.savetxt(data, "data_to2012_logrates_normed.txt")



