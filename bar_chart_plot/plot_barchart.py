import re
import os
import numpy as np
import matplotlib.pyplot as plt


def getData(filename):
    if 'temp.txt' in os.listdir(os.getcwd()):
        os.remove('.\\temp.txt')
    #print os.getcwd()
    filepath ='.\\pdf\\' + filename
    #print
    os.system(r'pdf2txt.py -p 3,4 -o temp.txt %s' %(filepath))
    #print os.getcwd()
    temp_file = open('temp.txt', 'r')
    layout = temp_file.readlines()
    pdfStr = ''
    for out in layout:
        pdfStr = pdfStr + str(out)

    temp_file.close()
    if 'temp.txt' in os.listdir(os.getcwd()):
        os.remove('.\\temp.txt')

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
    return final_data




pro_types = ['TCP Cubic', 'QUIC Cubic', 'TCP Vegas', 'SCReAM', 'PCC', 'TCP BBR', 'Verus', 'Sprout',
             'LEDBAT', 'FillP']
N = len(pro_types)
pdfPath = os.getcwd()+'\\pdf'
print pdfPath
pdfList = os.listdir(pdfPath)
#pdfpatt = '(.*?).pdf'

data = []
data.append(pro_types)
for i in pdfList:
    temp_data = []
    print i
    temp = getData(i)
    print temp
    for item in pro_types:
        i = 0
        while temp[0][i] != item:
            i += 1
        temp_data.append(100*float(temp[2][i])/12)
    data.append(temp_data)

print len(data)
print data

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
#rects1 = ax.bar(ind, men_means, width, color='r', yerr=men_std)
rects1 = ax.bar(ind, data[1], width, color='#3897FF')
#rects1 = ax.bar(ind, data[1], width,)
rects2 = ax.bar(ind + width, data[2], width, color='#F67088')
#rects2 = ax.bar(ind + width, data[2], width,)
#rects2 = ax.bar(ind + width, women_means, width, color='y', yerr=women_std)

# add some text for labels, title and axes ticks
ax.set_ylabel('Bandwidth Utilization (%)',fontsize = 14,y=0.4)
#ax.set_title('Chart of Protocols\' Bandwidth Utilization ')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(pro_types,rotation = 45,fontsize = 10)
ax.set_yticks([0,50,100,150],)

ax.legend((rects1[0], rects2[0]), (' 1   ACK every 100ms', '10 ACKs every 200ms'),loc = (0.33,0.73),
          fontsize = 11,facecolor = 'none')


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = float(rect.get_height())
        ax.text(rect.get_x() + rect.get_width()/2, height,
                '%.2f' % height,
                ha='center', va='bottom',fontsize = 8, rotation = -90)

autolabel(rects1)
autolabel(rects2)

fig = plt.gcf()
fig.set_size_inches(5, 3)
plt.subplots_adjust(left=0.14, bottom=0.25, right=0.98, top=0.94, wspace=0.2, hspace=0.2)
plt.savefig(r'./barchart.eps',format='eps')
plt.savefig(r'./barchart.png',format='png')
plt.show()
