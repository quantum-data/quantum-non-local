from os import listdir
import requests
from os.path import isfile, join
import json
import numpy as np


def analyze000(inp):
    win=0;
    for x,y in inp.items():
        a=0;b=0;c=0;
        for i in range(3):
            a+=int(x[2*i])
            b+=int(x[2*i+1])
            c+=int(x[2*i])^int(x[2*i+1])
        if (a%2==0 and b%2==0 and c%2==0): win+=y
    return win;

def analyze001(inp):
    win=0
    for x,y in inp.items():
        x=x[::-1]
        a1=int(x[5])
        b1=int(x[4])
        c1=(int(x[4])+int(x[5]))%2
        a2=int(x[3])
        b2=int(x[2])
        c2=(int(x[2])+int(x[3]))%2
        d3=(int(x[0])+int(x[1]))%2
        b3=int(x[0])
        e3=int(x[1])
        if ((b1+b2+b3)%2==0 and (a1+c1+a2+c2+d3+e3)%2==0):win+=y
    return win;

def analyze010(inp):
    win=0;
    for x,y in inp.items():
        x=x[::-1]
        a1=int(x[5])
        b1=int(x[4])
        c1=(int(x[4])+int(x[5]))%2
        a3=int(x[1])
        b3=int(x[0])
        c3=(int(x[1])+int(x[0]))%2
        d2=(int(x[3])+int(x[2]))%2
        b2=int(x[2])
        e2=int(x[3])
        if ((b1+b2+b3)%2==0 and (a1+c1+a3+c3+d2+e2)%2==0):win+=y
    return win;


def analyze011(inp):
    win=0;
    for x,y in inp.items():
        x=x[::-1]
        a1=int(x[5])
        b1=int(x[4])
        c1=(int(x[4])+int(x[5]))%2
        d2=(int(x[3])+int(x[2]))%2
        b2=int(x[2])
        e2=int(x[3])
        d3=(int(x[1])+int(x[0]))%2
        b3=int(x[0])
        e3=int(x[1])
        if ((b1+b2+b3)%2==0 and (a1+c1+d2+e2+d3+e3)%2==0 and (d2+e3+a1)%2==1):win+=y
    return win;

def analyze100(inp):
    win=0;
    for x,y in inp.items():
        x=x[::-1]
        a3=int(x[1])
        b3=int(x[0])
        c3=(int(x[1])+int(x[0]))%2
        a2=int(x[3])
        b2=int(x[2])
        c2=(int(x[3])+int(x[2]))%2
        d1=(int(x[4])+int(x[5]))%2
        b1=int(x[4])
        e1=int(x[5])
        if ((b1+b2+b3)%2==0 and (a3+c3+a2+c2+d1+e1)%2==0):win+=y
    return win;

def analyze101(inp):
    win=0;
    for x,y in inp.items():
        x=x[::-1]
        a2=int(x[3])
        b2=int(x[2])
        c2=(int(x[2])+int(x[3]))%2
        d1=(int(x[4])+int(x[5]))%2
        b1=int(x[4])
        e1=int(x[5])
        d3=(int(x[0])+int(x[1]))%2
        b3=int(x[0])
        e3=int(x[1])
        if (((b1+b2+b3)%2==0) and ((a2+c2+d1+e1+d3+e3)%2==0) and ((d3+e1+a2)%2==1)): win+=y
    return win;

def analyze110(inp):
    win=0;
    for x,y in inp.items():
        x=x[::-1]
        a3=int(x[1])
        b3=int(x[0])
        c3=(int(x[0])+int(x[1]))%2
        d2=(int(x[2])+int(x[3]))%2
        b2=int(x[2])
        e2=int(x[3])
        d1=(int(x[4])+int(x[5]))%2
        b1=int(x[4])
        e1=int(x[5])
        if ((b1+b2+b3)%2==0 and (a3+c3+d2+e2+d1+e1)%2==0 and (e2+d1+a3)%2==1):win+=y
    return win;

def analyze111(inp):
    win=0;
    for x,y in inp.items():
        x=x[::-1]
        d1=(int(x[4])+int(x[5]))%2
        b1=int(x[4])
        e1=int(x[5])
        d2=(int(x[3])+int(x[2]))%2
        b2=int(x[2])
        e2=int(x[3])
        d3=(int(x[1])+int(x[0]))%2
        b3=int(x[0])
        e3=int(x[1])
        if ((b1+b2+b3)%2==0 and (d1+e1+d2+e2+d3+e3)%2==0):win+=y
    return win;

def code(index):
    return ("000"+str((bin(index))[2:]))[-3:]

def analyze(index,inp):
    return globals()["analyze"+code(index)](inp)


def hist2dic(mymove) :
    hist=mymove['Histogram']
    dic={}
    for i in range(int(len(hist)/2)) :
        key=hist[2*i][1:12:2]
        dic[key]=hist[2*i+1]
    return dic


 
#### RETRIVING THE DATA

version="2"

onlyfiles = [f for f in listdir("out") if (isfile(join("out", f)) and f[-1]==version)]
alluri={}
alltext={}
for myfile in onlyfiles :
	f = open("out/"+myfile,) 
	js=json.load(f)
	uri=js['outputDataUri']
	name=js['name']
	alluri[name]=uri
	print("Loading "+name+"-->"+uri)
	r = requests.get(uri)
	alltext[name]=json.loads(r.text)

print(alltext)


move_dic=list(range(8))
move_dic_fixed=list(range(8))
cali_dic=list(range(4))

for i in range(8) :
	move_dic[i]=hist2dic(alltext['move'+str(i)+'.'+str(version)])

for i in range(4) :
	cali_dic[i]=hist2dic(alltext['move'+str(8+i)+'.'+str(version)])

tmp=cali_dic[1]
cali_dic[1]=cali_dic[2]
cali_dic[2]=tmp



###BUILDING CALIBRATION MATRIX



m= [[[0 for k in range(4)] for j in range(4)] for i in range (3)]
m[0][:][:]=[[0 for i in range(4)] for j in range(4)]
m[1][:][:]=[[0 for i in range(4)] for j in range(4)]
m[2][:][:]=[[0 for i in range(4)] for j in range(4)]
c=0
for k in range (4):
    for x,y in cali_dic[k].items():
        for i in range (3):
            for j in range (4):
                if (int(x[2*i])==j%2 and int(x[2*i+1])==int((j-j%2)/2)):
                    m[i][j][k]+=y
m1=m[0][:][:]
m2=m[1][:][:]
m3=m[2][:][:]
matrix=np.zeros((64,64))
for i in range(64):
    for j in range(64):
            matrix[i][j]=m1[i%4][j%4]*m2[int(i/4)%4][int(j/4)%4]*m3[int(i/16)%4][int(j/16)%4]
Cmatrix=np.linalg.inv(matrix)

def rewrite_y(inp):
    ys=[0]*64
    for x,y in inp.items():
        for i in range (64):
            if i==int(x,2):
                ys[i]=y
    new_ys=np.matmul(Cmatrix,ys)
    #new_ys=np.transpose(new_ys.reshape(8,8)).reshape(64)
    i=0
    count=0
    newinp={}
    for x,y in inp.items():
        for i in range (64):
            if i==int(x,2):
                newinp[x]=new_ys[i]
                if (newinp[x]>0):
                    count+=newinp[x]
                else:
                    newinp[x]=0
    newinp.update((x, y/count) for x, y in newinp.items())
    return newinp

##### ANALYZING RESULTS

win=list(range(8))
win_fixed=list(range(8))

for i in range(8) :
	win[i]=analyze(i,move_dic[i])
	move_dic_fixed[i]=rewrite_y(move_dic[i])
	win_fixed[i]=analyze(i,move_dic_fixed[i])
	print('move'+str(i)+': '+str((win[i]*100))+'% -->'+str((win_fixed[i]*100))+'%')


print('average: '+str((np.array(win).sum()*100/8))+'% -->'+str((np.array(win_fixed).sum()*100/8))+'%')






