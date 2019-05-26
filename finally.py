import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt

tb=pd.read_csv('statsallexomes1.txt', sep='\t',encoding='utf-8')
def op(k):
    hegh=pd.read_csv(k, sep=' ',encoding='utf-8')
    hegh=hegh.set_index('sample')
    hegh['concordantly']=hegh['concordantly'].str.strip()
    return hegh


gh=op('concordantstatisticsoral.txt')
dh=op('concordantstatisticsglio.txt')
fh=op('concordantstatisticspancr.txt')
jh=op('concordantstatisticsnsclc.txt')
mh=op('concordantstatisticsnasophar.txt')
tb=tb.set_index('sample')


jh['concordantly']=jh['concordantly'].str[:-1].astype(float)
jh=jh[jh.concordantly>80]

gh['concordantly']=gh['concordantly'].str[:-1].astype(float)
gh=gh[gh.concordantly>80]

fh['concordantly']=fh['concordantly'].str[:-1].astype(float)
fh=fh[fh.concordantly>80]

mh=mh.dropna()
mh=mh[~mh.concordantly.str.contains("Error")]
mh['concordantly']=mh['concordantly'].str[:-1].astype(float)
mh=mh[mh.concordantly>80]

dh['concordantly']=dh['concordantly'].str[:-1].astype(float)
dh=dh[dh.concordantly>80]

tb1=tb[['X','Y']]
tb1=tb1[tb1.X<1]

v=tb1['X'].median()
b=tb1['Y'].median()
def copynum(df):
    df['X']=df['X'].apply(lambda x:x/v)
    df['Y']=df['Y'].apply(lambda x:x/b)
    return df[['X','Y']]

def grap(df,name):

    ax=sns.boxplot(data=df)
    ax.set_xlabel('Chromosome')
    ax.set_ylabel('Copy number')
    plt.savefig(name+'.png', dpi=300)

grap(copynum(jh),'NSCLC')
grap(copynum(dh),'Glio')
grap(copynum(gh),'Oral')
grap(copynum(fh),'Pancreas')
grap(copynum(mh),'Nasophar')
