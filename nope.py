import numpy as np
import pandas as pd
import xlsxwriter as excel
from urllib.request import urlopen
import openpyxl
import pickle
sheets=[]
names=[]
import numpy as np
import pandas as pd
import xlsxwriter as excel
from urllib.request import urlopen
from openpyxl import load_workbook
import pickle
meme = pd.read_excel('pleasekillme.xlsx', sheet_name=None, usecols = 'A:C')

for name, sheet in meme.items():
    if any (char.isdigit() for char in name):
        continue
    else:
        gg=pd.DataFrame(sheet)
        sheets.append(gg)
        names.append(name)
for sheet, name in list(zip(sheets,names)):
    chrnum=[]
    sexchrs=[]
    tri=[]
    stri=[]
    di=[]
    tetra=[]
    length=[]
    chrtype=[]
    nope=[]
    xxy=[]
    xx=[]
    empty=[[] for i in range (0,6)]
    hollow=[[] for i in range (0,6)]
    sheet_index = sheet['Karyotype'].str.startswith('XY?') | sheet['Karyotype'].str.startswith('XX?')  | sheet['Karyotype'].str.startswith('X?')
    sheet1 = sheet[~sheet_index]
    sheet1=sheet1.reset_index()
    for index,row in sheet1.iterrows():
        kar=row['Karyotype']
        kar=str(kar)
        chrs=row['Modal Chromosome Number']
        if kar.startswith('XYY,') or kar.startswith ('XY,') and "-X" in kar and '+Y' in kar:
            nope.append((chrs,kar))
        if kar.startswith('XXY,'):
            xxy.append(kar)
        if kar.startswith('XX,'):
            xx.append(kar)
        if kar.startswith('XY,') and '+X' not in kar:
            empty[0].append('XY')
        elif kar.startswith('XX,') or kar.startswith('X,') and '+X' in kar:
            empty[1].append('XX')
        elif kar.startswith('X,'):
            empty[2].append('X')
        elif kar.startswith('XXY,') or kar.startswith('XY,') and '+X' in kar:
            empty[3].append('XXY')
        elif kar.startswith('XXYY,') or kar.startswith('XXYY') and "XXYYY" not in kar:
            empty[4].append('XXYY')
        else:
            empty[5].append((chrs,kar))
        if chrs>=62 and chrs<=76:
            tri.append(chrs)
        if chrs>=66 and chrs<=72:
            stri.append(chrs)
        if chrs>=77 and chrs<=98:
            tetra.append(chrs)
        if chrs>=41 and chrs<=61:
            di.append(chrs)
        if kar.startswith('XY,') and '+X' not in kar and chrs>=62 and chrs<=76:
            hollow[0].append(chrs)
        elif (kar.startswith('XX,') or kar.startswith('X,') and '+X' in kar) and chrs>=62 and chrs<=76:
            hollow[1].append(chrs)
        elif kar.startswith('X,') and chrs>=62 and chrs<=76:
            hollow[2].append(chrs)
        elif (kar.startswith('XXY,') or kar.startswith('XY,') and '+X' in kar) and chrs>=62 and chrs<=76:
            hollow[3].append(chrs)
        elif (kar.startswith('XXYY,') or kar.startswith('XXYY') and "XXYYY" not in kar) and chrs>=62 and chrs<=76:
            hollow[4].append(chrs)
        elif chrs>=62 and chrs<=76:
            hollow[5].append(chrs)
    total=len(sheet1)
    k=len(empty[0])/total
    l= len(empty[1])/total
    m=len(empty[2])/total
    n=len(empty[3])/total
    o=len(empty[4])/total
    p=len(empty[5])/total
    h=len(tri)/total
    z=len(tetra)/total
    w=len(di)/total
    xxy=(len(xxy)/total)*100
    xx=(len(xx)/total)*100
    stri=(len(stri)/total)*100
    if len(empty[0])==0:
        kt=0
    else:
        kt=len(hollow[0])/len(empty[0])
    if len(empty[1])==0:
        lt=0
    else:
        lt= len(hollow[1])/len(empty[1])
    if len(empty[2])==0:
        mt=0
    else:
        mt=len(hollow[2])/len(empty[2])
    if len(empty[3])==0:
        nt=0
    else:
        nt=len(hollow[3])/len(empty[3])
    if len(empty[4])==0:
        ot=0
    else:
        ot=len(hollow[4])/len(empty[4])
    if len(empty[5])==0:
        pt=0
    else:
        pt=len(hollow[5])/len(empty[5])
    fname=('nope')
    book=load_workbook(str(fname)+'.xlsx')
    df = pd.DataFrame(sheet1)
    writer = pd.ExcelWriter(str(fname)+'.xlsx', engine='openpyxl')
    writer.book = book
    df.to_excel(writer, sheet_name=name, startrow=0, startcol=0)
    df1 = pd.DataFrame({'XY': k*100,'XX,-Y': l*100,'X,-Y':m*100, 'XXY':n*100, 'XXYY':o*100, 'OTHER':p*100}, index=['% of Karyotype'])
    df2=pd.DataFrame({'Total Triploidy (62-76)':h*100,'Total Tetraploidy':z*100, 'Total Diploidy':w*100, 'Total XXY':xxy,'Total XX,-Y':xx,'Total Triploidy (66-72)':stri}, index=[0])
    df2.to_excel(writer, sheet_name=name, startrow=0, startcol=26)
    df3 = pd.DataFrame({'XY': kt*100,'XX,-Y': lt*100,'X,-Y':mt*100, 'XXY':nt*100, 'XXYY':ot*100, 'OTHER':pt*100}, index=['% of Triploidy'])
    df4 = pd.DataFrame({'XY': kt*k*100,'XX,-Y': lt*l*100,'X,-Y':mt*m*100,'XXY':nt*n*100,'XXYY':ot*o*100,'OTHER':pt*p*100}, index=['% of Triploid'])
    df5 = pd.DataFrame({'XY': k*100-kt*k*100,'XX,-Y': l*100-lt*l*100,'X,-Y':m*100-mt*m*100,'XXY':n*100-nt*n*100,'XXYY':o*100-ot*o*100,'OTHER':p*100-pt*p*100}, index=['% of Non-Triploid'])
    frames=[df1,df3,df4,df5]
    dfs=pd.DataFrame(empty[5])
    dfs.to_excel(writer,sheet_name=name,startrow=0,startcol=45)
    dfh=pd.DataFrame(nope)
    dfh.to_excel(writer, sheet_name=name,startrow=0, startcol=55)
    result=pd.concat(frames)
    result.to_excel(writer, sheet_name=name,startrow=0, startcol=20 )
    writer.save()
    writer.close()
