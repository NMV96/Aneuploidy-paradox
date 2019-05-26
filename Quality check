import os
import subprocess
dr1='/home/nelli/data/cancer_files/pancreatic/fastqs/'
dr2='/home/nelli/data/cancer_files/pancreatic/logs/'
dlist=os.listdir(dr1)
one=[]
two=[]
j=[]
for d in dlist:
  if d.endswith('1.fastq.gz'):
    one.append(d)
  elif d.endswith('2.fastq.gz'):
    two.append(d)
  else:
    continue
os.chdir(dr1)
two=[e for i in one for e in two if e.split('_')[0] in i]
samples=zip(one,two)

for i,(file1, file2) in enumerate(samples):
  if i==0:
    subprocess.call(["fastqc",file1,"--extract"])
  v=os.listdir(dr1)
  for h in v:
    if h.endswith('_fastqc'):
      path=dr1+h
      os.chdir(path)
      with open ("fastqc_data.txt","r") as f:
        f=f.read()
        f=f.splitlines(True)
        m=f[8]
        m=m.split()
        g={'Sequence length':m[-1]}
        for key,value in g.iteritems():
          if '-' in value:
            value=value.split('-')
          else:
            value=value

          if value<60 or (a<60 for a in value):
            j.append('Its snippy snippy time')
if len(j)>0:
  for file1,file2 in samples:
    name=file1.split('_')[0]
    n = open(dr2+name+"_cut.txt", "w")
    subprocess.call(["cutadapt","-j","12","-m","60", "-o", dr1+file1,"-p",dr1+file2, f
