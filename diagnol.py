l=[[1,2,3],[4,5,6],[7,8,9]]
k=len(l)
v=[]
for i in range(k-1,-1,-1):
    print(i)
    v.append(i)
for i in v[::-1]:
    v.append(-+v[i])
v.pop()
print(v)
b=[]
n=[]

for i in range(k):
    for j in range(k):
        if v[i]==(i-j):
            print(l[i])
            b.append(l[i])
    n.append(b)
    b=[]             
print(n)