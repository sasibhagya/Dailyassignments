#5 examples on extend

l=[10,20,30,40,50]
l.extend([60,70,80,90])
print(l)

l=[10,20,30,40,50]
l.extend([60,70,80,90]*2)
print(l)

'''l=[10,20,30,40,50]
l.extend([60,70,80,90]*[60,70,80,90])
print(l)#type error'''

l=[10,20,30,40,50]
m=[60,70,80,90]
l.extend(m)
print(l)

l=[10,20,30,40,50]
m=["bhagya","sasi"]
l.extend(m)
print(l)

l=[10,20,30,40,50]
l.extend(l[0:3])
print(l)

l=[10,20,30,40,50]
s=[]
for i in range(5):
    s.append(i)
l.extend(s)
print(l)



#5 examples on remove
l=[10,20,30,40,50]
l.remove(20)
print(l)

l=[10,20,30,40,50,"bhagya","sasi"]
l.remove("bhagya")
print(l)

'''l=[10,20,30,40,50,"bhagya","sasi"]
l.remove("Bhagya")
print(l)#value error'''

'''l=[10,20,30,40,50,"bhagya","sasi"]
l.remove(20,30)
print(l) #type error'''

l=[]
for i in range(1,21):
    l.append(i)
    if i%2==0:
        l.remove(i)
print(l)

#5 examples on pop

l=[10,20,30,40,50]
l.pop(2)
print(l)

l=[10,20,30,40,50]
l.pop()
print(l)

l=["bhagya","aman","sasi","vamsi"]
l.pop(1)
print(l)

'''l=[10,20,30,40,50,"bhagya","aman","sasi"]
l.pop(2,3)
print(l)#type error'''

l=["bhagya"]
l.pop()
print(l)

l=["bhagya",]
l.pop()
print(l)


#5 examples on reverse

l=[10,20,30,40,50]
l.reverse()
print(l)

l=["bhagya","aman","sasi","vamsi"]
l.reverse()
print(l)

'''l=["bhagya","aman","sasi","vamsi"]
l.reverse(l[0:2])
print(l) #type error'''

l=["bhagya"]
l.reverse()
print(l)

l=[10,20,30,40,"bhagya","aman","sasi","vamsi"]
l.reverse()
print(l)

#5 examples on sort

l=[10,20,30,40,50]
l.sort() 
print(l)

l=["bhagya","aman","sasi","vamsi"]
l.sort()
print(l)

'''l=[10,20,30,40,"bhagya","aman","sasi","vamsi"]
l.sort()
print(l) #typr error'''

'''l=[10,20,30,[70,80,90],40,50]
l.sort() 
print(l)#type error'''

l=["bhagya","Bhagya","bHagya",]
l.sort()
print(l)












