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


# pro_types = [ 'TACK-rich', 'TACK-poor','TCP BBR']#,'TCP CUBIC']
pro_types = [ 'TCP-TACK','TCP BBR']
# pro_types = [ 'PLR = 0 TCP-TACK', 'PLR = 0 TCP BBR','PLR = 1% TCP-TACK', 'PLR = 1% TCP BBR',]
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

# print (len(data))
# print (data)

ind = 2 * np.arange(N)  # the x locations for the groups
width = 0.85       # the width of the bars

# print (ind)

fig, ax = plt.subplots()
#rects1 = ax.bar(ind, men_means, width, color='r', yerr=men_std)
# rects1 = ax.bar(ind, data[1], width, color='#3897FF')
#rects1 = ax.bar(ind, data[1], width,)
# rects2 = ax.bar(ind + width, data[2], width, color='#F67088')
#rects2 = ax.bar(ind + width, data[2], width,)
#rects2 = ax.bar(ind + width, women_means, width, color='y', yerr=women_std)

yerrl = [[5,5,10,25],[5.5,6,12,26]]

plt.grid(alpha = 0.5)

#rects1 = ax.bar(ind[0],thrput[0] , width,color='#3897FF',edgecolor = 'white',capsize=5,yerr = yerrl[0][0])

for idx in range(len(ind)):
    rects1 = ax.bar(ind[idx]- width/2, data[1][idx], width,color='#3897FF',hatch="//",
                    edgecolor = 'white',yerr = yerrl[0][idx],capsize=2.5,error_kw={'barsabove':True})#capsize=5,error_kw={'uplims':True,'lolims':True,})
#     rects2 = ax.bar(ind[idx], data[2][idx],width,color='#389755')#,hatch="\\\\",edgecolor = 'white' )
    rects2 = ax.bar(ind[idx]+width/2 , data[2][idx], width, color='#F67088', 
                    edgecolor='white',yerr = yerrl[1][idx],capsize=2.5,error_kw={'barsabove':True})#,error_kw={'lolims':True,'uplims':True})
#     rects3 = ax.bar(ind[idx] + width, data[3][idx], width, color='#F67088', hatch="\\\\", edgecolor='white')
#    rects4 = ax.bar(ind[idx] + 2*width, data[4][idx], width, color='#557088', hatch="\\\\\\\\", edgecolor='white')
    autolabel(rects1,lbl[0][idx],xlbl[idx])
    autolabel(rects2,lbl[1][idx],xlbl[idx])
#     autolabel(rects3)
#    autolabel(rects4)

# add some text for labels, title and axes ticks
ax.set_ylabel('Goodput (Mbps)',fontsize = 16,y=0.5)
# ax.set_xlabel('Loss Rate on Return Path (%)',fontsize = 14,x=0.5)
#ax.set_title('Chart of Protocols\' Bandwidth Utilization ')
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
