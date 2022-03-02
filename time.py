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
c=0
for i in g:
    print(i)
while t==1:
    n=int(input("enter how many number of employee to conduct meetings :"))
    for i in range(n):
        f=id_s.index(input("enter employee name :   "))
        y.append(g[f])  
    #print(y,"erugfyhj")
   # print(y[0],"erugfyhj")
    u=copy.deepcopy(y) #assigning values
    for i in range(len(y)-1):
        for j in range(len(y[i])):
            if (y[i][j][1] > y[i+1][j][0] and y[i][j][0] < y[i+1][j][1])  and ((y[i+1][j][0] !=0  and y[i][j][1] !=0))   :
                c+=1
            if c==1:
                 res.append(y[i][j])
                 #print(y[i][j],"jgy")
            else:
                 res.append([0,0])    
            c=0
        #print(i,"is value",res)
        y[i+1]=res
        res=[]    
        t=0
y=y[-1]
p=[]#finding index whith there common timings
for i in y:
    if i != [0,0] :
        p.append(y.index(i))

#print(p)
t1=[]
c1=[]
#print(u,"thyos is u")

for i in p:
    for j in range(0,len(u)):
        t1.append(u[j][i])
    c1.append(t1)
    t1=[]
#print(c1)#common timings

k1=[]
n1=[]
c2=[]
c3=[]
for i in range(len(c1)):
    for j in range(len(c1[i])):
        for h in range(len(c1[i][j])//2):
            k1.append((c1[i][j][0]))
            n1.append((c1[i][j][-1]))
    c2.append(k1)
    c3.append(n1)
    k1=[]
    n1=[]
#print(c3)
#print(c2)
l1=[]
s2=[]
for i in range(len(c2)):
    for j in range(len(c3)//2):
        #print(max(c2[i]),":",min(c3[i]))
        s2.append([(max(c2[i])),(min(c3[i]))])
        l1.append(abs(max(c2[i])-min(c3[i])))
print(s2)
print("enter your meeting in minutes")
b1=int(input())
for i in l1:
    if b1<=i:
        print(s2[l1.index(i)])
        print() 

       
















'''[570, 600] jgy
[660, 769] jgy
[840, 1110] jgy
[630, 700] jgy
[780, 1080]
['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a0']
[[570, 600], [660, 769], [840, 1110]]
[[540, 615], [630, 700], [780, 1080]]
[[480, 540], [570, 772], [820, 1035]]
[[585, 616], [645, 729], [825, 1125]]
[[535, 660], [675, 774], [840, 1075]]
[[630, 660], [690, 826], [885, 1110]]
[[585, 600], [605, 788], [855, 1130]]
[[615, 645], [665, 826], [895, 1160]]
[[670, 675], [690, 753], [810, 1215]]
[[555, 576], [590, 817], [895, 1095]]'''