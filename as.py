def ct(i,dur,g,tp):
    flag = 0
    for x in tp:
        for y in g[x]:
            if (i in range(y[0],y[1]+1)) and (i+dur in range(y[0],y[1]+1)):
                flag += 1
                break  
    if flag == len(tp):
        return True
    else :
        return False
import pandas as pd
import csv
import copy
c=["ID","empname","cit1","cot1","cit2","cot2","cit3","cot3"]
r=pd.read_csv("SampleData.csv",usecols=c)
l=[]
p=[]
for i in range(2,len(c)):
    l.append(list(r[c[i]]))
m=[]
b=[]
for i in range(len(l[0])):
    for j in range(len(l)):
        b.append(l[j][i])
    m.append(b)
    b=[]
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
t=1
y=[]
res=[]
id_s=list(r[c[0]])
print(id_s)
g=copy.deepcopy(b)
d=[]
c=0
for i in g:
    print(i)
t=1
while t:
    st=[]
    tp=list(map(str ,input("enter employee id").split()))
    dur=int(input("enter duration"))
    sm=0
    ind=[]
    for i in tp:
        ind.append(id_s.index(i))

    for i in ind:
        for j in g[i]:
            st.append(j[0])
    st=sorted(st)
    print(st)
    for n in st:
        if ct(n,dur,g,ind):
            sm=n
            break
    print(sm, sm+dur)
    for x in ind:
            for l,y in enumerate(g[x]):
                if sm in range(y[0], y[1]):
                    if sm== y[0]:
                        y[0] = sm+dur
                    elif sm== y[1]:
                        y[1] = sm
                    else:
                        g[x].append([y[0], sm])
                        g[x].append([sm+dur, y[1]])
                        del g[x][l]               
    for i in ind:
        print(sorted(g[i]))
    print("do u want to continue y/n")
    o=input()
    if o=="y":
        t=1
    else:
        t=0

