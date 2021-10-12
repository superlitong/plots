from bs4 import BeautifulSoup
import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from ast import literal_eval
import re
# toy_df['valval'] = toy_df['valval'].apply(lambda s:literal_eval(s))[0]

del_patt = '0:0'

def soup_to_df(soup):
    date = str(soup.tbody.a).split('\n')[1].strip()
    date_lst = []
    date_lst.append(date)
    trace_lst = []
    vv_lst = []
    for i in range(20):
        tr_content = soup.tbody.findAll('tr')[i]
        trace = str(tr_content.findAll('td')[0]).split('\n')[1].strip()
        trace_lst.append(trace)
        vv_lst_1 = []
        for j in range(24):
    #         print(i)
    #         print(tr_content.findAll('td')[j+1])
            try:
                val_lst = tr_content.findAll('td')[j+1]['data-content'].split('\n')
                vv = []
                for val in val_lst:
                     vv.append(val.strip().strip('<br>'))
                vv_lst_1.append(vv)   
            except:
                vv_lst_1.append(['0:0','0:0','0:0','0:0'])  #后续数据处理时删除
        vv_lst.append(vv_lst_1)   

    soup_df['date'] = date_lst*len(trace_lst)
    soup_df['trace'] = trace_lst
    soup_df['valval'] = vv_lst

# def get_fillp_rank(s): 
#     score_lst = []
#     fillp_score = float(s[4][0].split(':')[1].strip().replace('&minus;','-'))      
#     for i in range(len(s)):
#         score_lst.append(float(s[i][0].split(':')[1].strip().replace('&minus;','-')))
#     score_lst = sorted(score_lst)
#     score_lst.reverse()
#     fillp_rank = score_lst.index(fillp_score) + 1
#     return fillp_rank

def get_rank(s,i): 
    #得到某个协议在某天某个场景的测试排名
    score_lst = []
    score = float(s[i][0].split(':')[1].strip().replace('&minus;','-'))      
    for i in range(len(s)):
        score_lst.append(float(s[i][0].split(':')[1].strip().replace('&minus;','-')))
    score_lst = sorted(score_lst)
    score_lst.reverse()
    rank = score_lst.index(score) + 1 #排名从1开始
    return rank

# t_val = []
# for i in to_use_proto_idx:
#     t_val.append(result_df['valval'][0][i])
def filter_index(s):
    t_val = []
    for i in to_use_proto_idx:
        t_val.append(s[i])
    return t_val


def label_zero_proto_lst(s):
    re_lst = re.findall(del_patt,str(s))
    if len(re_lst) > 0:
        return 1
    else:
        return 0

result_df = pd.read_csv('pantheon_rank_200day.csv',index_col=0)

result_df['valval'] = result_df['valval'].apply(lambda s:literal_eval(s))


all_proto = ['TCP BBR',
'Copa',
'TCP Cubic',
'FillP',
'FillP-Sheep',
'Indigo',
'Indigo-MusesC3',
'Indigo-MusesC5',
'Indigo-MusesD',
'Indigo-MusesT',
'LEDBAT',
'Muses_DecisionTree',
'Muses_DecisionTreeH0',
'Muses_DecisionTreeR0',
'PCC-Allegro',
'PCC-Expr',
'QUIC Cubic',
'SCReAM',
'Sprout',
'TaoVA-100x',
'TCP Vegas',
'Verus',
'PCC-Vivace',
'WebRTC media']
to_use_proto = ['TCP BBR','Copa','TCP Cubic','FillP-Sheep','Indigo','PCC-Allegro','QUIC Cubic','Sprout','TCP Vegas','Verus','PCC-Vivace']

to_use_proto_idx = []
#得到用来进行比较排名协议的index
for val in to_use_proto:
    to_use_proto_idx.append(all_proto.index(val))

result_df['to_use_val'] = result_df['valval'].apply(lambda s:filter_index(s))

result_df['is_all_tested'] = result_df['to_use_val'].apply(lambda s:label_zero_proto_lst(s))
#筛选有所有协议测试结果的数据
result_df = result_df[result_df.is_all_tested==0].reset_index(drop=True)
print("selected columns:",result_df.shape[0])

#得到用来画图的数据
proto_lst = []
rank_lst = []
rank_a_lst = []
for i in range(len(to_use_proto)):
#     print(i)
    a = []
    a.append(to_use_proto[i])
    rank_lst.extend(list(result_df['to_use_val'].apply(lambda s:get_rank(s,i))))
    proto_lst.extend(a*result_df.shape[0])

violin_df = pd.DataFrame()
violin_df['proto'] = proto_lst
violin_df['rank'] = rank_lst
violin_df['median'] = violin_df.groupby(['proto'])['rank'].transform('median') 
#小提琴图中的x轴按中位数大小顺序排列
violin_df.sort_values(by='median',inplace=True)

list(violin_df.groupby(['proto'])['rank'].agg('median').reset_index().sort_values(by='rank').proto)

violin_df['rank'].min()
violin_df['median'].unique()
violin_df[violin_df.proto=='Sprout'].min()

sns.set(style="ticks")
# ax = sns.violinplot(x="proto", y="rank", 
#                      data=violin_df, palette="deep",order=['FillP-Sheep',
#  'TCP Cubic',
#  'Copa',                                                         
#  'Indigo',
#  'TCP BBR',
#  'PCC-Vivace',
#  'PCC-Allegro',
#  'Sprout',
#  'TCP Vegas',
#  'Verus',
#  'QUIC Cubic'])

# ax = sns.violinplot(x="proto", y="rank", 
#                      data=violin_df, palette=sns.color_palette("", 13),
#                      width=1.2,cut=0,inner='box' )

ax = sns.violinplot(x="proto", y="rank", 
                     data=violin_df,  palette=sns.color_palette("hls", 13),
                     width=1.2,cut=0,inner='box',linewidth=1,zorder=30 )

# list(violin_df.groupby(['proto'])['rank'].agg('median').reset_index().sort_values(by='rank').proto)
for i,l in enumerate(ax.lines):
    if i%2==0:
        plt.setp(l,linewidth=2,linestyle='-',solid_capstyle='butt')
    elif i%2==1:
        plt.setp(l,linewidth=6,linestyle='-',solid_capstyle='butt')
    
        
plt.gcf().set_size_inches(8,3)
plt.xticks(rotation=90,fontsize=13)
ax.set_xticklabels(['TCP Vegas',
 'TCP-TACK',
 'TCP CUBIC',
 'Indigo',
 'PCC-Vivace',
 'Copa',
 'TCP BBR',
 'PCC-Allegro',
 'QUIC CUBIC',
 'Verus',
 'Sprout'])
tiks = [2*i+1 for i in range(6) ]
plt.yticks(tiks,fontsize=14)
plt.ylabel('Ranking (smaller is better)',fontsize=14)
plt.xlabel('',fontsize=0)
median_lst = list(violin_df.drop_duplicates(subset=['proto'])['median'])
for i in range(11):
    ax.scatter(i,median_lst[i],color='w',marker='.',edgecolors='w',s=80,zorder=20)
plt.savefig('fillp_rank_pantheon.png',bbox_inches='tight',dpi=300,pad_inches=0)
plt.savefig('fillp_rank_pantheon.eps',bbox_inches='tight',dpi=300,pad_inches=0)
plt.savefig('fillp_rank_pantheon.pdf',bbox_inches='tight',dpi=300,pad_inches=0)

