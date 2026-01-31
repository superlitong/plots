#!/usr/bin/python3
# -*- coding: utf-8 -*-
import numpy as np
import random
import matplotlib.pyplot as plt
from cProfile import label
import statsmodels.api as sm
import os
plt.switch_backend('agg')
font1 = {
'weight' : 'normal',
'size'   : 17,
}
colors = [ "#305089", '#A43337','#F4B664', '#99C09C',"#5D9FC4" , "#0F0F0F"]
markersize =7
linewidthx = 2.5
markevery1 = 4
legend_size = 7
gridlinewidth = 1.5
lss = ['-',"--","dotted",":","-."]
markers = ["o","p","<",">","^"]
loads = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]

figs = (4,2.7)

plt.cla()
plt.figure(figsize=figs)
large_avg_pcn = np.array(large_avg_pcn)
large_avg_ecn = np.array(large_avg_ecn)
large_avg_tcn = np.array(large_avg_tcn)
# large_avg_codel = np.array(large_avg_codel)
plt.plot(loads,np.ones(9),label="DiffECN",color=colors[0],linewidth=linewidthx,markersize=markersize,marker=markers[0])
plt.plot(loads,large_avg_ecn/large_avg_pcn,label="ECN",color=colors[1],linewidth=linewidthx,markersize=markersize,marker=markers[1])
plt.plot(loads,large_avg_tcn/large_avg_pcn,label="TCN",color=colors[2],linewidth=linewidthx,markersize=markersize,marker=markers[2])
plt.legend()
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel("Load", font1)
plt.ylabel("Normalized FCT", font1)
yslim =[0.8, 1.8]
plt.ylim(yslim)
plt.grid(linestyle="--", linewidth=gridlinewidth)
plt.tight_layout()
plt.savefig("large_avg.png",format="png")
plt.savefig("large_avg.pdf",format="pdf")
