import os 
import subprocess
os.chdir('/home/nelli/data/cancer_files/nsclc/fastqs/')
dr1='/home/nelli/data/cancer_files/nsclc/fastqs/'
dr2='/home/nelli/data/cancer_files/nsclc/alignments/'
dlist=os.listdir(dr1)
one=[]
two=[]
for d in dlist:
  if d.endswith('1.fastq.gz'):
    one.append(d)
  elif d.endswith('2.fastq.gz'):
    two.append(d)
  else:
    continue

two=[e for i in one for e in two if e.split('_')[0] in i]
samples=zip(one,two)
indexBaseName="/data/db/hg38ensembl/hg38ensembl"

for file1, file2 in samples:
  name=file1.split('_')[0]
  if not os.path.isfile(dr2+name+".sam"): 
    f = open("/home/nelli/data/cancer_files/pancreatic/logs/"+name+".txt", "w")
    subprocess.call(["bowtie2","--fast", "-p", "12", "-x", indexBaseName, "-1", file1, "-2", file2, "-S", dr2+name+".sam"], stderr=f)
