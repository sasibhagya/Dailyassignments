a=[10,20,30,40,50]
b=a[1:]
print(id(a))
print(id(b))
print(b)
print()

a=[10,20,30,40,50]
b=a
print(id(a))
print(id(b))
print(b)
print()

#list object comparision

a=[10,20,30,40,50]
b=[10,20,30,40,50]
print(id(a))
print(id(b))
print(a==b)  #here also ids are different but it checks the values only not ids
print()

print(id(a))
print(id(b))
print(a is b) #but here it check ids
print()

a=["bhagya","sasi","prahya","riyanshi"]
b=["bhagya","sasi","prahya","riyanshi"]
print(id(a))
print(id(b))
print(a==b)  #here also ids are different but it checks the values only not ids
print()

print(id(a))
print(id(b))
print(a is b) #but here it check ids
print()

a=[10,20,30,40,50,"bhagya","sasi","prahya","riyanshi"]
b=[10,20,30,40,50,"bhagya","sasi","prahya","riyanshi"]
print(id(a))
print(id(b))
print(a==b)
print() 

print(id(a))
print(id(b))
print(a is b)
print() 

a=[10,20,30,40,50,"bhagya","sasi","prahya","riyanshi"]
b=["bhagya","sasi","prahya","riyanshi",10,20,30,40,50]
print(id(a))
print(id(b))
print(a==b)
print() 

print(id(a))
print(id(b))
print(a is b) 
print()


#*****nested list in a matrix form

l=[[10,20,30],[40,50,60],[70,80,90]]
for i in range(len(l)):
    for j in range(len(l[i])):
        print(l[i][j],"",end="")
    print()


#list comprehension

#square root of range from 1 to 20
l=[x*x for x in range(1,21)]
print(l)

# do some action in l1 and use l1 in l2
l1=[x*x for x in range(1,11)]
print(l1)
l2=[i for i in l1 if i%2==0]
print(l2)