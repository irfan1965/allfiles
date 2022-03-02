import pandas as pd
import csv
import copy
c=["ID","empname","cit1","cot1","cit2","cot2","cit3","cot3"]
r=pd.read_csv("SampleData.csv",usecols=c)
l=[]
p=[]
#l.append([r["cit1"],r["cot1"]])
for i in range(2,len(c)):
    l.append(list(r[c[i]]))
#print(l)
m=[]
b=[]
for i in range(len(l[0])):
    for j in range(len(l)):
        b.append(l[j][i])
    m.append(b)
    b=[]
#print(m,"irfan")
v=[]
b=[]
j=0
for i in range(0,len(m)):
    while j<len(m[i])-1: 
            v.append([m[i][j],m[i][j+1]])
            j+=2
    b.append(v)
    v=[]
    j=0
#print(b)
t=1
y=[]
res=[]
id_s=list(r[c[0]])
print(id_s)
g=copy.deepcopy(b)
d=[]
for i in g:
    print(i)
while t==1:
    n=int(input("enter how many number of employee to conduct meetings :"))
    for i in range(n):
        f=id_s.index(input("enter employee name :   "))
        y.append(g[f])
        
    
    c=0
    for i in range(n-1):
        for j in range(len(g[0])):
            for k in range(1):
                if (y[i][j][1] > y[i+1][j][0])  and ((y[i+1][j][0] !=0  and y[i][j][1] !=0) and y[i][j][0] < y[i+1][j][1])  :
                     c+=1
            if c==1:
                 res.append(y[i][j])
            else:
                 res.append([0,0])    
            c=0
        g[i+1]=res
        d.append(g[i+1])
        res=[]    
        t=0
print(d[-1])