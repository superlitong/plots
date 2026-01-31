#!/usr/bin/env python
import numpy as np
from collections import defaultdict
from numpy import *
import matplotlib.pyplot as plt
from cProfile import label
import statsmodels.api as sm
import os
font1 = {
'weight' : 'normal',
'size'   : 17,
}

colors = [ "#305089", '#A43337','#F4B664', '#99C09C',"#5D9FC4" , "#7373B9", '#D2B48C']
data = []
# hatchs = ['/', '\\', '-', 'x', 'o', '.', '*']
hatchs = ['O', '*', '\\', 'o', 'x', '/', '.']
markersize =7
linewidthx = 4
markevery1 = 4
legend_size = 7
gridlinewidth = 1.5
fct_completion_by_bucket = defaultdict(list)
put_completion_by_bucket = defaultdict(list)

if __name__ == '__main__':
    ECNMQ_PATH = '../load0.1/mix-ECN-MQ/one/fct_topology_WebSearch_distributionincast20_dcqcn.txt'
    ECNPORT_PATH = '../load0.1/mix-ECN-PORT/one/fct_topology_WebSearch_distributionincast20_dcqcn.txt'
    PCN_PATH = '../load0.1/mix-PCN/two/fct_topology_WebSearch_distributionincast20_dcqcn.txt'


    plt.figure(figsize=(5,3)) #创建绘图对象

    y_time = pcn
    x_tcp = np.linspace(min(y_time), max(y_time))
    # x_elp = np.linspace(min(y_noincast), max(y_noincast))
    tcp_ecdf = sm.distributions.ECDF(y_time)
    # elp_ecdf = sm.distributions.ECDF(y_noincast)
    y_time_ = tcp_ecdf(x_tcp)
    # y_noincast_ = elp_ecdf(x_elp)
    plt.plot(x_tcp/1000, y_time_, label='DiffECN', color = colors[0], linewidth = linewidthx, linestyle = '-')





    y_time = ecnport
    x_tcp = np.linspace(min(y_time), max(y_time))
    # x_elp = np.linspace(min(y_noincast), max(y_noincast))
    tcp_ecdf = sm.distributions.ECDF(y_time)
    # elp_ecdf = sm.distributions.ECDF(y_noincast)
    y_time_ = tcp_ecdf(x_tcp)
    # y_noincast_ = elp_ecdf(x_elp)
    plt.plot(x_tcp/1000, y_time_, label='ECN', color = colors[1], linewidth = linewidthx, linestyle = ':')

    y_time = ecnmq
    x_tcp = np.linspace(min(y_time), max(y_time))
    # x_elp = np.linspace(min(y_noincast), max(y_noincast))
    tcp_ecdf = sm.distributions.ECDF(y_time)
    # elp_ecdf = sm.distributions.ECDF(y_noincast)
    y_time_ = tcp_ecdf(x_tcp)
    # y_noincast_ = elp_ecdf(x_elp)
    plt.plot(x_tcp/1000, y_time_, label='MQ-ECN', color = colors[2], linewidth = linewidthx, linestyle = '--')

    plt.legend(fontsize=13)
    plt.grid(linestyle="--", linewidth=gridlinewidth)
    plt.xlabel("Small flow FCT/ms", font1)
    plt.ylabel("CDF", font1)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    # plt.gcf().subplots_adjust(left=0.14, bottom=0.19, right=0.99, top=0.96, wspace=0.2, hspace=0.2)
    plt.tight_layout()
    plt.savefig('test_slowdown1.png', format='png')
    plt.savefig('test_slowdown1.pdf', format='pdf')
