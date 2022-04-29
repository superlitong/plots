# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt


def autolabel(rects,lbl,x):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = float(rect.get_height())+x
        ax.text(rect.get_x() + rect.get_width()/2, height,
                '%.0f' % lbl,
                ha='center', va='bottom',fontsize = 12, rotation = 0)


pro_types = [ 'TCP-TACK','TCP BBR']
xlabels = ['802.11\nb','802.11\ng','802.11\nn','802.11\nac']
N = 4

#坐标转换后绘图数据
data = []
data.append(pro_types)
data.append([30,120,298,556]) 
data.append([25,95,255,434])

#原始数据用户bar上的标注
lbl = []
lbl.append([6,23.5,198,556]) 
lbl.append([5.4,19,155,434]) 

#调整标注距离
xlbl = [2.5,2.5,5,20]

ind = 2 * np.arange(N)  # the x locations for the groups
width = 0.85       # the width of the bars


fig, ax = plt.subplots()

yerrl = [[5,5,10,25],[5.5,6,12,26]]

plt.grid(alpha = 0.5)

for idx in range(len(ind)):
    rects1 = ax.bar(ind[idx]- width/2, data[1][idx], width,color='#3897FF',hatch="//",
                    edgecolor = 'white',yerr = yerrl[0][idx],capsize=2.5,error_kw={'barsabove':True})
    rects2 = ax.bar(ind[idx]+width/2 , data[2][idx], width, color='#F67088', 
                    edgecolor='white',yerr = yerrl[1][idx],capsize=2.5,error_kw={'barsabove':True})

    autolabel(rects1,lbl[0][idx],xlbl[idx])
    autolabel(rects2,lbl[1][idx],xlbl[idx])


# add some text for labels, title and axes ticks
ax.set_ylabel('Goodput (Mbps)',fontsize = 16,y=0.5)


ax.set_xticks(ind)
ax.set_xticklabels(xlabels,rotation = 0,fontsize = 12)
ax.set_yticks([0,150,300,400,500,600])
ax.set_yticklabels([0,30,200,400,500,600],fontsize=12) 
ax.set_ylim([0,660])
ax.legend((rects1[0], rects2[0]), pro_types,loc = 'upper left',
          ncol=1,fontsize = 14,facecolor = 'none',columnspacing =0.1)#,bbox_to_anchor = (0.41,1))

fighdr=plt.gcf()
fighdr.set_size_inches(4,3)

# plt.subplots_adjust(left=0.16, bottom=0.17, right=0.99, top=0.99, wspace=0.2, hspace=0.2)

plt.savefig(r'./Acks_Packets_barchart.pdf',format='pdf',pad_inches=0,bbox_inches = 'tight',dpi=300)
plt.savefig(r'./Acks_Packets_barchart.eps',format='eps',pad_inches=0,bbox_inches = 'tight',dpi=300)
plt.savefig(r'./Acks_Packets_barchart.png',format='png',pad_inches=0,bbox_inches = 'tight',dpi=300)
plt.show()
