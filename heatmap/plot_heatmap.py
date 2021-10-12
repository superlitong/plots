# coding=utf-8
import os
import re
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from math import log

def calcEff(filename):

    if 'temp.txt' in os.listdir(os.getcwd()):
        os.remove('.\\temp.txt')
    #print os.getcwd()
    os.system(r'pdf2txt.py -p 3,4 -o temp.txt %s' %filename)
    print os.getcwd()
    temp_file = open('temp.txt', 'r')
    layout = temp_file.readlines()
    pdfStr = ''
    for out in layout:
        pdfStr = pdfStr + str(out)

    temp_file.close()
    #print pdfStr
    #pdfStr = pdfStr + out.get_text()
    pdfStr = str(pdfStr)
    patt = 'mean loss rate \(\%\)\s+scheme(.*?)Run 1: Statistics of'
    m = re.findall(patt,pdfStr,re.S)
    #print len(m)
    #print m[0]
    final_data=[]

    sub_m = m[0].split('# runs')
    temp_sub_m = sub_m[0].replace('\n\n', '\n')
    final_data.append(temp_sub_m.split('\n'))
    #da = sub_m[1].split(u'\ufb02ow 1')
    da = sub_m[1].split(u'\u94ff\u4ff9w 1')
    for i in range(len(da)):
        temp = da[i].replace('\n\n', '\n')
        final_data.append(temp.split('\n'))

    for i in range(len(final_data)):
        while '' in final_data[i]:
            final_data[i].remove('')

    #print final_data
    final_data = np.array(final_data)
    #计算 log(mean throughput / mean 95th percentile delay)
    protocolList = []
    protocolEfficency = []
    pro_types = ['TCP Cubic', 'QUIC Cubic', 'TCP Vegas', 'SCReAM', 'PCC', 'TCP BBR', 'Verus', 'Sprout',
                 'LEDBAT', 'FillP']
    for item in pro_types:
        i = 0
        while final_data[0][i] != item:
            i += 1
        protocolList.append(final_data[0][i])
        protocolEfficency.append(log(float(final_data[2][i]) / float(final_data[3][i]), 2))

    #print protocolList
    #print protocolEfficency
    return protocolEfficency


#创建热图
def creatHeatMap(array,ylabel):
    pro_types = ['TCP Cubic', 'QUIC Cubic', 'TCP Vegas', 'SCReAM', 'PCC', 'TCP BBR', 'Verus', 'Sprout', 'LEDBAT', 'FillP']
    #y轴标签ylabels
    uniform_data = array
    ylabels = ylabel
    pro_types_num = len(pro_types)
    ylabels_num = len(ylabels)
    uniform_data1 = []
    for i in range(ylabels_num):
        uniform_data[i] = [float(j) for j in uniform_data[i]]

    uniform_data = np.array(uniform_data)
    #print uniform_data
    #print type(uniform_data)

    for i in range(ylabels_num):
        print uniform_data[i]
        temp = np.argsort(- uniform_data[i])
        temp1 = [0]* pro_types_num
        j= 0
        for j in range(pro_types_num):
            temp1[temp[j]] = j + 1
        #print temp1
        uniform_data1.append(temp1)
        #print uniform_data1[i]
    print uniform_data1

    sns.set()
    #fig = plt.figure()
    #ax = fig.add_subplot(1,2,2)
    ax = plt.subplots(figsize=(14, 8))
    ax = sns.heatmap(uniform_data1, vmin=0, vmax=9, center= 13,xticklabels=pro_types, yticklabels=ylabels,\
                     annot=True)
    ax.tick_params(axis = 'y', labelsize = 10)
    ax.tick_params(axis='x', labelsize=10)
    ax.set_xticklabels(ax.get_xticklabels(), rotation = -45,fontsize = 10,)
    ax.set_yticklabels(ax.get_yticklabels(), rotation = 0,fontsize =10 ,y=0)
    ax.xaxis.tick_top()
    #ax.set_title('heat map')
    colorbar = ax.collections[0].colorbar
    colorbar.set_ticks([0, pro_types_num - 1])
    colorbar.set_ticklabels(['Best','Worst'])
    fig = plt.gcf()
    #fig.set_size_inches(10,6)
    plt.subplots_adjust(left= 0.22,bottom=0.08,right=0.93,top=0.87,wspace=0.2,hspace=0.2)
    plt.savefig(r'./Heatmap.eps', format='eps')
    plt.savefig(r'./Heatmap.png', format='png')
    plt.show()

def main():
    dataList = []
    pdfPath = os.getcwd()+'\\pdf'
    #print pdfPath
    pdfList = os.listdir(pdfPath)
    for i in pdfList:
        dataList.append(calcEff(pdfPath+'\\'+i))

    #pdfpatt = '\w+\-\w+\-to\-\w+\-\w+'
    pdfpatt = '\d+\-\d+\-\d+T\d+\-\d+\-(.*?)\-10\-runs'
    pl = re.findall(pdfpatt,str(pdfList))
    title = []
    for i in pl:
        temp_title=''
        temp = i.split('-')
        for j in range(10):
            if  str(j) in temp:
                temp.remove(str(j))
                
        for item in temp:
            temp_title += item+' '
        
        title.append(temp_title)

    #creatHeatMap(dataList, pl)
    creatHeatMap(dataList, title)

if __name__ == '__main__':
    main()
