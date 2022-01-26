import matplotlib.pyplot as plt
import numpy as np
import math as mt
import json
f = open('data_to2012__size_rate_lograte', 'r')
data = []
for line in f:
    subreddit, data = line.split("\t")
    year = subreddit.strip("[]\n").split(",")[1]
    size = data.strip("[]\n").split(",")[0]
    rate = data.strip("[]\n").split(",")[1]
    lograte = data.strip("[]\n").split(",")[2]
    data.append(lograte)
f.close()

np.savetxt(data, "data_to2012_logrates.txt")

mean = np.mean(data)
data = [x/mean for x in data if x>0]

np.savetxt(data, "data_to2012_logrates_normed.txt")



