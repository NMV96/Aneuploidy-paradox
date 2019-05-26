import os
import re
import pandas as pd
import numpy as np

path='/home/nelli/data/cancer_files/papillary_thyr_ca/logs/'
path1='/home/nelli/data/cancer_files/papillary_thyr_ca/'
os.chdir(path)
lal=os.listdir(path)


con=[]
for d in os.listdir(path):

  if os.stat(d).st_size == 0:
    con.append((d.split('.')[0],'Error'))
  else:
    with open(d, 'r') as f:
      for line in f.readlines():
        if 'aligned concordantly exactly 1 time' in line:
           con.append((d.split('.')[0],re.findall('\(([^)]+)', line)[0]))
con=pd.DataFrame(con, columns=['sample','concordantly'])
con=con.set_index('sample')
print(con)

j=pd.read_csv(path1+'statsallexomes_thyroid.txt', sep='\t', encoding='utf-8')
lal=[d.split('.')[0] for d in lal]
j=j.set_index('sample')
j=j.loc[lal]
j['concordantly']=con['concordantly']
j.to_csv(path1+"concordantstatistics.txt", sep=' ')
  
