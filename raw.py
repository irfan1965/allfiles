import csv
import copy
r=open("lot.csv")
k=csv.reader(r)
j=[]
for i in k:
  j.append(i)
g=copy.deepcopy(j)
dic={ }
c=0
x=[]
for i in range(1,len(g)):
  x.append(g[i][0])
#print(x)
temp={}
td={}
for i in x:
  temp[i]=[]
  td[i]=[]
u=[]
for i,j in dic.items():
  print(i,j)
for i  in g[1:]:
  dic[i[0]]=i[1:]
class Vehicle:
    def __init__(self,Name,Number):
        self.Name=Name
        self.Number=Number
class bike(Vehicle):
    def __init__(self,Name,Number):
        #print(Name,Number)
        Vehicle.__init__(self,Name,Number)
class car(Vehicle):
    def __init__(self,Name,Number):
        #print(Name,Number)
        Vehicle.__init__(self,Name,Number)
class bus(Vehicle):
    def __init__(self,Name,Number):
        #print(Name,Number)
        Vehicle.__init__(self,Name,Number)
f=1
while( f==1):
  o=input("enter vehicle type")
  if o=="car":
      sp=0
      ep=6
      name=input("enter car name")
      number=input("enter car number")
      obj=car(name,number)
  elif o=="bike":
      sp=6
      ep=9
      name=input("enter bike name  :  ")
      number=input("enter bike number  :   ")
      obj=bike(name,number)
  else:
      name=input("enter bus name  :  ")
      number=input("enter bus number  : ")
      obj=bus(name,number)
      sp=9
      ep=10
  c=0
  for i,j in dic.items():
    for v in range(sp,ep):
      if j[v]=="free" :
        temp[i].append(v)
        td[i].append([name,number])
        print(td)
        print("|------------------------------------|")
        print("|your token number   :      |1A12{}{}| |".format(str(i),str(v)))
        print("|------------------------------------|")
        c=1
        j[v]="occupied"
        break
    if(c==1):
      break
  
  #print(temp)
  #print("your token number")
  for i ,j in temp.items():
    if len(j)>=1:
      print("Do you Want to de allocate y/n ")
      b=input()
      if b=="y":
        n=input("enter your lot number ")
        #print(temp.index(temp[n[0]][int(n[1])]) ,"uydr")
        #print(temp[n[0]][temp[n[0]].index(int(n[1]))] ,temp[n[0]],"ytwef")
        try:
          if temp[n[0]][temp[n[0]].index(int(n[1]))] in temp[n[0]]:
            m=float(input("enter how many hours"))
            print()
            print()
            print("YOUR PARKING DETAILS --->")
            if m<=1 and m>0 :
              print("|------------------------------------|")
              print("20 rupees only")
            elif m<=10:
              m=m*10
              print("|------------------------------------|")
              print("|your charges will be :     {}     ".format(m))
            else: 
              m=m*5
              print("|------------------------------------|")
              print("|your charges will be :     {}     ".format(m))

            dic[n[0]][int(n[1])]="free"
            #print(temp["A"].index(int(n[1])),"index")
            #print(td)
            #print(temp)
            print("|your car name    :     {}           ".format( td[n[0]][temp[n[0]].index(int(n[1]))][0]))
            print("|your car number   :     {}          ".format( td[n[0]][temp[n[0]].index(int(n[1]))][1]))
            print("|------------------------------------|")
            print()
            print()

            td[n[0]].remove(td[n[0]][temp[n[0]].index(int(n[1]))])
            temp[n[0]].remove(temp[n[0]].index(int(n[1])))
            #print(temp)
            #print(n[0],n[1])      
        except Exception :
            print("enter details correctly")
        
  f=int(input("enter 1 to park  :  "))

  
