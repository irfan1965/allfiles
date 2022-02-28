import copy
from math import *
# import csv
# k=[]
# l=[]
# n=csv.reader(open("Student_Data.csv"))
# print("number of line %d"%(n.line_num))
# for i in n :
#     l.append(i)
    

# for i in l:
#     for k in i:
#          print(k,end=" ")
#     print()

#l=[["A","B","c","D","E","F"],]
o=["A","B","C"]
print(o)
l=[
[[9,10],[10,11],[1,3],[4,5]],
[[9,10],[11,12],[12,3],[4,6]],
[[9,11],[12,1],[1,3],[4,5]]
 ]
# for i in l:
#     print(i)
g=copy.deepcopy(l)
for i in range(len(l)):
    for j in range(len(l[i])):
        for k in range(len(l[i][j])):
            if l[i][j][k]<6:
                l[i][j][k]=l[i][j][k]+12
            l[i][j][k]=l[i][j][k]*60     
    print()

t=1
y=[0,1]#index

# while t:
#     n=int(input("enter how many number employee to conduct meetings :"))
#     for i in range(n):
#         m=o.index(input("enter employee name"))
#         y.append(m)
#     for i in range(len(l[0])):
print(g[0])
print(g[1])
#        l
#print(l[0][1])
#print(l[1][1])
c=0
for i in range(ceil(len(y)/2)):
    for j in range(len(l[0])):
        for k in range(2):
            if g[i][j][k] in range(g[i+1][j][0],g[i+1][j][1]+1):
                 #print(g[i][j][k],g[i+1][j][0],g[i+1][j][1])
                 c+=1
            elif g[i+1][j][k] in range(g[i][j][0],g[i][j][1]+1):
                 c+=1
        if c==2:
            print(g[i][j])
            pass
        c=0


        

