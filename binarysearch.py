l=[1, 2, 3, 34, 43, 45, 65, 98,100]
l=sorted(l)
print(l)
o=int(input("enter which element to be search"))
f=0
h=len(l)-1
m=(f+h)//2
while l[m]!=o:
    if l[m]<o:
        f=m+1
    else:
        h=m-1
    m=(f+h)//2
print(m)

        