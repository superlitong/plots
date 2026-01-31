import matplotlib.pyplot as plt
import numpy as np

colors = [ "#305089", '#A43337','#F4B664', '#99C09C',"#5D9FC4" , "#7373B9", '#D2B48C']
data = []
# hatchs = ['/', '\\', '-', 'x', 'o', '.', '*']
hatchs = ['O', '*', '\\', 'o', 'x', '/', '.']
linewidthx = 2.5
font1 = {
'weight' : 'normal',
'size'   : 16,
}

gridlinewidth = 1.5
width=0.35
fig = plt.figure(figsize=(5,3))
ax1 = fig.add_subplot(111)
ax1.bar(x-width/2, y1, width, label='Utilization', color = 'white', edgecolor = colors[0], hatch = hatchs[0], linewidth=linewidthx, alpha=0.8)
ax1.legend(bbox_to_anchor=(0.16, 0.85),loc=3, borderaxespad=0, fontsize=13)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14)

plt.xticks(x,[r'DiffECN', r'MQ-ECN', r'ECN'])
ax1.set_ylabel("Link Utilization", font1)
ax1.set_ylim(0,1.1)
ax2 = ax1.twinx()
ax2.bar(x+width/2, y2, width, label='PFC', color='white',edgecolor = colors[1], hatch=hatchs[1], linewidth=linewidthx, alpha=0.8)
ax2.set_ylim(0,26)
ax2.legend(bbox_to_anchor=(0.56, 0.85),loc=3, borderaxespad=0, fontsize=13)
ax2.set_ylabel("PFC Pause Rate/Mbps", font1)
ax1.annotate('0.87', xy=(1-0.35/2, 0.87), xytext=(0,3), textcoords="offset points", ha='center', va='bottom', fontsize=13)
ax1.annotate('0.83', xy=(2-0.35/2, 0.83), xytext=(0,3), textcoords="offset points", ha='center', va='bottom', fontsize=13)
ax1.annotate('0.79', xy=(3-0.35/2, 0.79), xytext=(0,3), textcoords="offset points", ha='center', va='bottom', fontsize=13)
ax2.annotate('9.55', xy=(1+0.35/2, 9.55), xytext=(0,3), textcoords="offset points", ha='center', va='bottom', fontsize=13)
ax2.annotate('11.53', xy=(2+0.35/2+0.02, 11.53), xytext=(0,3), textcoords="offset points", ha='center', va='bottom', fontsize=13)
ax2.annotate('23.08', xy=(3+0.35/2, 23.08), xytext=(0,3), textcoords="offset points", ha='center', va='bottom', fontsize=13)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# plt.xticks(fontsize=26)

# plt.gcf().subplots_adjust(left=0.14, bottom=None, right=0.88, top=0.96)
plt.tight_layout()
plt.savefig('twoy.pdf', format='pdf')
plt.savefig('twoy.png', format='png')