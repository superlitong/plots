# coding=utf-8
import os
import re
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def creatScatter(data,title):
    pro_types = ['TCP Cubic', 'QUIC Cubic', 'TCP Vegas', 'SCReAM', 'PCC', 'TCP BBR', 'Verus', 'Sprout', 'LEDBAT',
                 'FillP']
    #sourcedata = file('data.csv','rb')
    #datareader = list(csv.reader(sourcedata, delimiter=','))
    datareader = data
    #print type(datareader)

    symble = ['x','d','o','s','*','p','+','v','1','8']
    color = ['b','c','g','k','m','r','b','y','k','m']

    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    #ax1 = plt.subplots(figsize=(14, 8))
    #ax1.set_title(title,fontsize = 8)
    ax1.set_yticks([0,300,600,900])
    #mpatches.Arrow(200, 600, 0.1, 0.1,width=0.1)
    #ax1.set_yticks()
    plt.xlabel('95th Percentile One-way Delay (ms)',fontsize = 14)
    plt.ylabel('Average Throughput (Mbit/s)',fontsize = 14,y=0.42)

    #plt.text(200, 600, 'Better ', size=8, color='r')
    delay = []
    throuput = []
    for item in pro_types:
        i = 0
        while datareader[0][i] != item:
            i += 1
        throuput.append(float(datareader[2][i]))
        delay.append(float(datareader[3][i]))
        #ax1.plot(x,y,c = color[i],marker = symble[i])

    print throuput
    print delay
    for i in range(len(pro_types)):
        ax1.scatter(delay[i], throuput[i], s=40, c=color[i], marker=symble[i])
    #ax1.legend( (1,2,3,4,5,6,7,8),labels = pro_types, loc = 'upper right')
    ax1.legend( (1,2,3,4,5,6,7,8,9,10), labels = pro_types, bbox_to_anchor=(1.02,0.5),
                loc = 'center left',fontsize = 10,handleheight = 1.2,handlelength= 0.3,markerscale = 1)
    xend = 0.3 *(max(delay)-min(delay)) + min(delay)
    yend = 0.8 * 900
    #xtextend = 0.5 *(delay[len(pro_types)] - delay[0])
    #ytextend = 0.5 * 900
    #rr =

    #plt.annotate('Better', xy=(150, 700), xytext=(200, 450), rotation=-45,
                 #bbox=dict(boxstyle="square", ec=(1., 0.5, 0.5), fc=(1., 0.8, 0.8), ),
                 #arrowprops=dict(facecolor='Red', shrink=0.05, alpha=0.4))

    plt.text(xend, yend, ' Better ', rotation=-40,size=12,
             bbox=dict(boxstyle="larrow", ec=(1., 0.5, 0.5), fc=(1., 0.8, 0.8),alpha = 0.5, ))
    fig = plt.gcf()
    fig.set_size_inches(5,3)
    plt.subplots_adjust(left=0.14, bottom=0.16, right=0.75, top=0.97, wspace=0.2, hspace=0.2)
    tt = title.split('\n')
    plt.savefig(r'./%s.eps'%tt[0], format='eps')
    plt.savefig(r'./%s.png'%tt[0], format='png')
    #plt.show()

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

def main():
    dataList = []
    pdfPath = os.getcwd()+'\\pdf'
    print pdfPath
    pdfList = os.listdir(pdfPath)
    pdfpatt = '(\d\d\d\d\-\d\d\-\d\d)(T\d\d\-\d\d\-)([\-|\w|\d]*)\-pantheon\-report\.pdf'
    for i in pdfList:
        print i
        pl = re.findall(pdfpatt, str(i))
        title = str(pl[0][0])+' test from '+str(pl[0][2]).replace('-',' ')+\
                ' of 30s each per scheme\n(mean of all runs by scheme)'
        data = getData(i)
        creatScatter(getData(i),title)

if __name__ == '__main__':
    main()

