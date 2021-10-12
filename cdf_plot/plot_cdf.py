import pandas as pd
import sys
import os
import re
import argparse
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="darkgrid")
import warnings 
warnings.filterwarnings('ignore')

def findlog(path,ret):
    filelist = os.listdir(path)
    for filename in filelist:
        de_path = os.path.join(path, filename)
        if os.path.isfile(de_path):
            if de_path.endswith(".log"): #Specify to find the txt file.
                ret.append(de_path)
        else:
            findlog(de_path,ret)
            
            
#process log

log = []
findlog('.',log)

patt = 'recv_list_bytes: (\d+)'

rtt_patt = 'rtt(\d+)_'
plr_patt = 'plr(\d+)_'

v_lst = []
t_lst = []
rtt_lst = []
plr_lst = []
for file in log:
    vallst = []
    typelst = []
    rttlst = []
    plrlst = []
    plr = re.findall(plr_patt,file)
    rtt = re.findall(rtt_patt,file)
    with open(file) as f:
        file_content = f.read().split('\n')
        for ctnt in file_content:
            a = re.findall(patt,ctnt)
            if len(a) != 0:
                rttlst.extend(rtt)
                plrlst.extend(plr)
                vallst.extend(a)
                if file.split('.')[1][-2:] == 'NN':
#                     print(1)
                    typelst.append('NN')
                else:
                    typelst.append('WN')
    v_lst.extend(vallst)
    t_lst.extend(typelst)
    rtt_lst.extend(rttlst)
    plr_lst.extend(plrlst)


df_tu = pd.DataFrame()
df_tu['bytes_recvd'] = v_lst
df_tu['type'] = t_lst
df_tu['rtt'] = rtt_lst
df_tu['plr'] = plr_lst
df_tu['bytes_recvd'] = df_tu['bytes_recvd'].astype(int)

df_tu['a'] = df_tu['type']+'_'+df_tu['rtt']+'_'+df_tu['plr']

df_tu.head(5)            
            
def plot_cdf(df_tus,h,ll):    
    """
    h:hue
    ll:legend_out
    """
    df_to_use = df_tus.copy()
#     print(df_to_use.columns)
    df_to_use = df_to_use[df_to_use.bytes_recvd!=0]
    df_to_use['bytes_recvd'] = df_to_use['bytes_recvd'].apply(lambda s:np.log10(s*1472))
    #edit legend labels
    label_noIACK = 'Without IACK'
    label_withIACK = 'With IACK'
    df_to_use['type'] = df_to_use['type'].apply(lambda s:label_noIACK if s=='NN' else label_withIACK)

    sns.set(style='ticks',font='Arial')

    _, bins = np.histogram(df_to_use["bytes_recvd"],bins=100)

    #xx_palette = ['blue','k']   #自定义palette
    g = sns.FacetGrid(df_to_use, hue=h,palette='deep',despine=False,legend_out=True,
                      hue_kws={"kde_kws" : [dict(cumulative=True,linestyle='--',linewidth=2),
                                           dict(cumulative=True,linestyle='-',linewidth=4)]})
    g.map(sns.distplot, "bytes_recvd", bins=bins,hist_kws=dict(cumulative=True),
                 hist=None)
    
    if ll:
        plt.legend(fontsize=13)
    else:
        g.add_legend()
#     bbox_to_anchor=(0.56, 0.7)
    plt.grid()
    #plt.xticks(fontsize=14)
   # plt.yticks(fontsize=14)
    plt.xlabel('Data Blocked in Receive Buffer(Byte)',fontsize=14)
    plt.ylabel('CDF',fontsize=14)
    g.set_xticklabels(["100","1K","10K","100K","1M","10M","100M"])
    fighdr=plt.gcf()
    fighdr.set_size_inches(4,3)
    plt.savefig('rcv_inflight_IACK.png',bbox_inches='tight',pad_inches=0)
    plt.savefig('rcv_inflight_IACK.eps',bbox_inches='tight',pad_inches=0,dpi=300)
    plt.savefig('rcv_inflight_IACK1.pdf',bbox_inches='tight',dpi=300,pad_inches=0)
    plt.show()            
            
            
            
            
            
            
