#!/usr/bin/python3
# -*- coding: utf-8 -*-
import numpy as np
import random
import matplotlib.pyplot as plt
from cProfile import label
import statsmodels.api as sm
from collections import defaultdict
import os
plt.switch_backend('agg')
font1 = {
'weight' : 'normal',
'size'   : 17,
}
colors = [ "#305089", '#A43337','#F4B664', '#99C09C' , "#7373B9"]
colors = [ "#305089", '#A43337','#F4B664', '#99C09C',"#5D9FC4" , "#0F0F0F", '#00FFFF']
colors = [ "#305089", '#A43337','#F4B664', '#99C09C',"#5D9FC4" , "#0F0F0F", '#00FFFF']
# colors = [ "#99C09C", '#7373B9','#F4B664', '#305089',"#272727" , "#A43337"]
hatchs = ['O', '*', '\\', 'o', 'x', '-']
markersize =7
linewidthx = 2.5
markevery1 = 4
legend_size = 7
gridlinewidth = 1.5
lss = ['-',"--","dotted",":","-."]
markers = ["o","p","<",">","^"]

plt.figure(figsize=(4,3)) #创建绘图对象
x = np.arange(4)
width = 0.15  # 柱子的宽度
# total_width, n = 1, 3
# width = total_width/n
x3 = x
x1 = x3-width*2
x2 = x3-width
x4 = x3+width
x5 = x3+width*2

# x = np.arange(4)  # x轴刻度标签位置

# 计算每个柱子在x轴上的位置，保证x轴刻度标签居中
# x - width，x， x + width即每组数据在x轴上的位置
# plt.bar(x - width, y1, width, label='1')
# plt.bar(x, y2, width, label='2')
# plt.bar(x + width, y3, width, label='3')
# plt.bar(x - width*2, y1, width, label='1')
# plt.bar(x + width*2, y1, width, label='1')
plt.bar(x1,y1,width=width,color='white',edgecolor = colors[0], label="0.8RTT", hatch=hatchs[0], linewidth=linewidthx) #00cc33  / 008000  00CCFF  00ff00
plt.bar(x2,y2,width=width,color='white',edgecolor = colors[1],label="1.0RTT", hatch=hatchs[1], linewidth=linewidthx)
plt.bar(x3,y3,width=width,color='white',edgecolor = colors[2],label="1.5RRT", hatch=hatchs[2], linewidth=linewidthx)
plt.bar(x4,y4,width=width,color='white',edgecolor = colors[3],label="2.0RTT", hatch=hatchs[3], linewidth=linewidthx)
plt.bar(x5,y5,width=width,color='white',edgecolor = colors[4],label="2.5RTT", hatch=hatchs[4], linewidth=linewidthx) #{'/', '\', '|', '-', '+', 'x', 'o', 'O', '.', '*'}
# plt.bar(x1,all_tcp,width=width,color='white',edgecolor = colors[1],label="TCP", hatch='/')
# plt.bar(x2,all_wrdma,width=width,color='white',edgecolor = colors[0], label="WDTCP", hatch='\\') #00cc33  / 008000  00CCFF  00ff00
plt.xticks(x,[r'0.6', r'0.7', r'0.8', r'0.9'],fontsize=14)
plt.yticks([5,6,7,8],['5', '6', '7', '8'],fontsize=14)
plt.legend(fontsize = 12)
# plt.legend(bbox_to_anchor=(0.5, 0.6), loc=3, borderaxespad=0, fontsize = 12)
# plt.legend(loc=(0.05, 0.45), fontsize=12, frameon = 0)
# plt.legend(bbox_to_anchor=(0.1, 1.02),loc=3, borderaxespad=0,fontsize=17, ncol=2)
# plt.legend(loc='best')
plt.ylim(5)
plt.xlabel("load", font1)
plt.ylabel("Throughput/Gbps", font1)
# plt.gcf().subplots_adjust(left=0.13, bottom=0.19, right=0.99, top=0.85, wspace=0.2, hspace=0.2)
# plt.gcf().subplots_adjust(left=0.132, bottom=0.19, right=0.99, top=0.96, wspace=0.2, hspace=0.2)
plt.tight_layout()
plt.savefig(r'throughput_edge.png', format='png')
plt.savefig(r'throughput_edge.pdf', format='pdf')