y=[
    [[585, 600], [605, 665], [675, 788],[1131,1232]], 
    [[670, 645], [895, 1160]]
   ]  
m1=[]
for i in y:
        m1.append(len(i))

q=max(m1)
print(m1)
r1=y[m1.index(q)]
print(r1,"dht")
print(y[0][0],len(y[0][0]),"eg")
for i in range(len(y)):
    if len(y[0][i])<q:
        for j in range(len(y[i])):
            if  y[i][j][0] < r1[j][1]:
                print(y[i][j][0] , r1[j][1])
                pass
            else:
                    y[i].insert(r1.index(r1[j]),[0,0])
                    print("hi")
                    break
    print(i)
print(y)