n=int(input())
p=[]
for i in range(n):
    l=list(map(int,input().split()))
    p.append(l)
print(p)
k=[]
o=[]
for i in range(len(p)):
  for j in range(len(p)):
    k.append(p[j][i])
  o.append(k)
  k=[]
for i in o:
  print(i)