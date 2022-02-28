import copy
o=["A","B","C","D"]
print(o)
l=[
[[9,10],[10,11],[1,3],[4,5]],
[[9,10],[11,12],[12,3],[4,6]],
[[9,11],[12,1],[1,3],[4,5]],
[[8,10],[12,14],[4,4],[4,5]]
 ]

g=copy.deepcopy(l)
for i in range(len(l)):
    for j in range(len(l[i])):
        for k in range(len(l[i][j])):
            if l[i][j][k]<=6:
                g[i][j][k]=g[i][j][k]+12
            l[i][j][k]=l[i][j][k]*60     
    print()

t=1
y=[]
r=[]
while t==1:
    n=int(input("enter how many number of employee to conduct meetings :"))
    for i in range(n):
        b=o.index(input("enter employee name :   "))
        y.append(g[b])
        print(g[b])
    
    c=0
    for i in range(n-1):
        for j in range(len(l[0])):
            for k in range(1):
                if y[i][j][1]  > y[i+1][j][0]  and (y[i+1][j][0] !=0  and y[i][j][1] !=0):
                    c+=1
            if c==1:
                r.append(y[i][j])
            else:
                r.append([0,0])    
            c=0
        g[i+1]=r
        print(g[i+1],"sdf")
        r=[]    
        t=0
print()