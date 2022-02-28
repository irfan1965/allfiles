import random
m=list(map(str,input("enter :  ").split()))
#m=['irfan','is','a','good','hoax!']
p=""
s=""
for n in m:
    if len(n)>3:
        p=n[1:len(n)-1]
        p=list(p)
        random.shuffle(p)
        g=n[0]
        for i in p:
            if i.isalpha():
                g+=i
            else:
                s+=i
        g+=n[-1]
        print(g,end=" ")
    else:
        print(n,end=" ")
print(s)