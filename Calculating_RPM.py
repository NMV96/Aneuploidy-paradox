import numpy as np
import pandas as pd
import os
tabs=list()
path='/home/nelli/data/cancer_files/nsclc/statistics1/'
os.chdir(path)
dlist=os.listdir(path)
dlist=[d for d in dlist if d.endswith('_statistics.txt')]
col=['Chromosome','Chromosome length','Exon length']
ff=pd.read_csv('/data/nelli/exonlength.txt', sep='\t', encoding='utf-8', names=col)
cff=ff[['Chromosome','Exon length']]
cff['Chromosome']=cff['Chromosome'].apply(lambda x:x.split('r')[1])
clist=['1','10',	'11',	'12',	'13',	'14',	'15',	'16',	'17',	'18',	'19',	'2',	'20',	'21',	'22',	'3',	'4',	'5',	'6',	'7',	'8',	'9',	'X',	'Y']
cff=cff.set_index('Chromosome')
cff=cff.loc[clist]
def nor(x):
  cnames=('ref.seq.name','ref.seq.length','n_mapped','n_unmapped')
  df=pd.read_csv(x,sep="\t",header=None,encoding="utf-8", names=cnames)
  df['sample']=x.split('_')[0]
  np.r_[0:22, 23:25]
  cdf=df.iloc[np.r_[0:22, 23:25]]
  cdf['exon.length']=cff['Exon length'].values
  tabs.append(cdf)

for d in dlist:
  nor(d)

sf=pd.concat(tabs)

sf['mappedreads']=(sf['n_mapped'].div(sf['exon.length'], axis=0))*1000000
tabl=pd.pivot_table(sf,index=['sample'],values=['mappedreads'], columns=['ref.seq.name'] )
tabl=tabl.round(2)
tabl.columns=['1','10',	'11',	'12',	'13',	'14',	'15',	'16',	'17',	'18',	'19',	'2',	'20',	'21',	'22',	'3',	'4',	'5',	'6',	'7',	'8',	'9',	'X',	'Y']
med=tabl.drop(['X','Y'], axis=1)
med=med.median(axis=1)
tabl['median']=med.round(2)

tabl1=tabl.div(tabl['median'], axis=0).round(2)
tabl1=tabl1.drop('median', axis=1)
tabl1.to_csv('/home/nelli/data/cancer_files/nsclc/statsallexomesnsclc1.txt', sep='\t', encoding='utf-8')
```
