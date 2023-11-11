
#break
for i in range(1,101):
    if i==50:
        break
    print(i)


name="bhagya"
for i in name:
    if i=="g":
        break
    print(i)


list=[10,20,30,40,50]
for i in list:
    if i>40:
        break
    print(i)


a=[10,20,30,-40,50,20]
sum=0
for i in a:
    if i<=0:
        break
    sum=sum+i
print(sum)

names=["bhagya","sasi","john","mahika","prahya"]
for i in names:
    if i=="john":
        break
    print(i)

#continue:
for i in range(1,10):
    if i==5:
        continue
    print(i)

    
a=[10,20,30,-40,50,20]
sum=0
for i in a:
    if i<=0:
        continue
    sum=sum+i
print(sum)


name="bhagya"
for i in name:
    if i=="g":
        continue
    print(i)

list=[10,20,30,40,50,60,70,25,36,11]
for i in list:
    if i>40:
        continue
    print(i)

names=["bhagya","sasi","john","mahika","prahya"]
for i in names:
    if i=="john":
        continue
    print(i)


#pass

for i in range(1,11):
    if i==5:
        print("hello")
    else:
        pass


a="bhagya"
for i in a:
    pass

for i in range(1,11):
    if i==5:
        pass
    else:
        print("hello")



name=input("enter the name: ")
for i in name:
    pass

for i in range(5):
    print("hey")
    for j in range(10):
        if j>5:
            print("hi")
        else:
            pass
print("bhagya")

