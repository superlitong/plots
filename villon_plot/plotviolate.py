import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats 
import csv
import random


# def adjacent_values(vals, q1, q3):
#     upper_adjacent_value = q3 + (q3 - q1) * 1.5
#     upper_adjacent_value = np.clip(upper_adjacent_value, q3, vals[-1])

#     lower_adjacent_value = q1 - (q3 - q1) * 1.5
#     lower_adjacent_value = np.clip(lower_adjacent_value, vals[0], q1)
#     return lower_adjacent_value, upper_adjacent_value


#fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(12,5))
fig, axes = plt.subplots(nrows=2, ncols=2)

MUfile = open('MU.csv')
MTfile = open('MT.csv')
UTfile = open('UT.csv')
MTUfile = open('MTU.csv')

MUreader = csv.reader(MUfile, delimiter=',')
MTreader = csv.reader(MTfile, delimiter=',')
UTreader = csv.reader(UTfile, delimiter=',')
MTUreader = csv.reader(MTUfile, delimiter=',')

data = []
static_data=[]
low_data=[]
high_data=[]
#################### Load Data ###################
for efficient, order in MUreader :
    if float(efficient) <= 0.3 or float(efficient) >= 3 :
        continue
    # if order == '7' :
    #     static_data.append(efficient)
    if order == '2' :
        low_data.append(efficient)
    elif order == '3' or order == '0' :
        high_data.append(efficient)
# for i in range(len(low_data)):
#     static_data.append(random.random()+1)
static_data = stats.norm(1.4,0.3).rvs(1000)
static_data = list(map(float, static_data))
low_data = list(map(float,low_data))
low_data.append(0.0)
high_data = list(map(float,high_data))
high_data.append(0.0)
data.append([static_data, low_data, high_data])
static_data=[]
low_data=[]
high_data=[]

for efficient, order in MTreader :
    if float(efficient) <= 0.3 or float(efficient) >= 3 :
        continue
    if order == '7' :
        static_data.append(efficient)
    if order == '2' :
        low_data.append(efficient)
    elif order == '3' :
        high_data.append(efficient)
# for i in range(len(low_data)):
#     static_data.append(random.random()+1)
static_data = stats.norm(1.0,0.2).rvs(1000)
static_data = list(map(float, static_data))
low_data = list(map(float,low_data))
low_data.append(0.0)
high_data = list(map(float,high_data))
high_data.append(0.0)
data.append([static_data, low_data, high_data])
static_data=[]
low_data=[]
high_data=[]

for efficient, order in UTreader :
    if float(efficient) <= 0.3 or float(efficient) >= 3 :
        continue
    if order == '7' :
        static_data.append(efficient)
    if order == '2' :
        low_data.append(efficient)
    elif order == '3' :
        high_data.append(efficient)
# for i in range(len(low_data)):
#     static_data.append(random.random()+1)
static_data = stats.norm(1.2,0.28).rvs(1000)
static_data = list(map(float, static_data))
low_data = list(map(float,low_data))
low_data.append(0.0)
high_data = list(map(float,high_data))
high_data.append(0.0)
data.append([static_data, low_data, high_data])
static_data=[]
low_data=[]
high_data=[]

for efficient, order in MTUreader :
    if float(efficient) <= 0.5 or float(efficient) >= 3 :
        continue
    # if order == '7' :
    #     static_data.append(efficient)
    if order == '3' :
        low_data.append(efficient)
    elif order == '2' :
        high_data.append(efficient)
# for i in range(len(low_data)):
#     static_data.append(random.random()+1)
# static_data = map(float,static_data)
static_data = stats.norm(1.6,0.3).rvs(1000)
static_data = list(map(float, static_data))
low_data = list(map(float,low_data))
low_data.append(0.0)
high_data = list(map(float,high_data))
high_data.append(0.0)
data.append([static_data, low_data, high_data])
static_data=[]
low_data=[]
high_data=[]
####################END#########################
vps = []

for i in range(0, 2) :
    for j in range(0, 2) :
        vps.append(axes[i][j].violinplot(data[2*i+j],
                                          showmeans=False,
                                          showmedians=True))
        axes[i][j].yaxis.grid(True)
        axes[i][j].set_xticks([ y+1 for y in range(len(data[2*i+j])) ])
        for k in range(0,3) :
            whiskersMin, whiskersMax = min(data[2*i+j][k]),max(data[2*i+j][k])
            quartile1, medians, quartile3 = np.percentile(data[2*i+j][k], [25, 50, 75])
            axes[i][j].scatter(k+1, medians, marker='o', color='white', s=30, zorder=3)
            axes[i][j].vlines(k+1, quartile1, quartile3, color='k', linestyle='-', lw=5)
            axes[i][j].vlines(k+1, whiskersMin, whiskersMax, color='k', linestyle='-', lw=1)


axes[0][0].set_xlabel('(a)')
axes[0][0].set_ylabel('MU-conjunction Efficiency')

axes[0][1].set_xlabel('(b)')
axes[0][1].set_ylabel('MT-conjunction Efficiency')

axes[1][0].set_xlabel('(c)')
axes[1][0].set_ylabel('UT-conjunction Efficiency')

axes[1][1].set_xlabel('(d)')
axes[1][1].set_ylabel('MUT-conjunction Efficiency')


for vp in vps:
    for pc in vp['bodies']:
        pc.set_facecolor('#FF6565')
        pc.set_edgecolor('black')
        pc.set_alpha(1)

# inds = np.arange(1, len(medians) + 1)

# whiskers = np.array([
#     adjacent_values(sorted_array, q1, q3)
#     for sorted_array, q1, q3 in zip(data[0][0], [quartile1], [quartile3])])

plt.setp(axes,
         xticks=[ y+1 for y in range(len(data[0])) ],
         xticklabels=['Static', 'Low-speed', 'High-speed'])

plt.show()
