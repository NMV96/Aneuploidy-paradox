import os
import numpy as np
import pandas as pd
import subprocess
x=pd.read_csv("/data/nelli/PRJNA386668pancreas ductal adenosquamous.txt",sep="\t", encoding="utf-8")
y=pd.read_csv("/data/nelli/newtablespancreaticductaladenosquamous.txt", sep="\t", encoding="utf-8",  header=None)
k=[]
odd=[]
one=[]
two=[]
for index,row in y.iterrows():
  k.append(list(row)[0].split(',')[1])

for index, row in x.iterrows():
  sam=row['secondary_sample_accession']
  fastq=row['fastq_ftp']
  for g in k:
    if g in sam:
      if len(fastq.split(';'))==3:
        odd.append(fastq.split(';')[0])
        one.append(fastq.split(';')[1])
        two.append(fastq.split(';')[2])
      elif len(fastq.split(';'))==2:
        one.append(fastq.split(';')[0])
        two.append(fastq.split(';')[1])
os.chdir('/data/nelli/cancer_files/pancreatic/fastqs/')
l=list(zip(one,two))
for a,b in l:
  if not os.path.isfile(a.split('/')[-1]) or not os.path.isfile(b.split('/')[-1]):
    subprocess.call(['wget',a,b])
