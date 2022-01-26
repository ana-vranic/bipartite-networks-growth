import matplotlib.pyplot as plt
import math as mt
import json
import numpy as np
f = open('data_to2012_size_rate_lograte', 'r')

data = []
for line in f:
    year, data = line.split("\t")
    size = data.strip("[]\n").split(",")[1]

    data.append(size)

f.close()

np.savetxt(data, "reddit2012_sizes.txt")


mean = np.mean(data)
data = [x/mean for x in data if x>0]

np.savetxt(data, "reddit2012_sizes_normed")


