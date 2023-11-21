# 5 examples on index
name="python is a programming language and it is very simple"
print(name.index("is"))# found 1st is
print(name.index("p"))#1st p
print(name.index("lan"))#even print half word it is showing
print(name.index("a",0,20))
#print(name.index("b"))#substring not found error

#5examples on count
name="python is a programming language and it is very simple"
print(name.count("a"))
print(name.count("is"))
print(name.count("are"))
print(name.count("b"))
print(name.count("ve"))
print(name.count("vet"))

#5examples on insert
l=[1,2,3,4,5]
l.insert(2,10)
print(l)

l=[1,2,3,4,5]
l.insert(0,20)
print(l)

l=[1,2,3,4,5]
l.insert(5,20)
print(l)

l=[1,2,3,4,5]
l.insert(4,20)
print(l)

l=[1,2,3,4,5]
l.insert(10,20)
print(l)

#5examples on append

l=[1,2,3,4,5]
l.append(99)
print(l)

l=[1,2,3,4,5]
l.append(20)
print(l)

l=[]
s=10,20,30
l.append(s)
print(l)

l=[]
s=[10,20,30]
l.append(s)
print(l)

'''l=1
s=[10,20,30]
l.append(s)
print(l)  # attributeerror

s=[10,20,30]
s.append(10,20)
print(l)  #type error'''


l=[1,0.5,True,"bhagya"]
print(l)

#accessing elements from the list using while
l=[10,20,30,40]
s=0
while s<len(l):
    print(s)
    s=s+1

l=[10,20,30,40]
i=0
while i<len(l):
    print(l[i])
    i=i+1

l=[]
for j in range(11):
    l.append(j)
i=0
while i<len(l):
    print(l[i],"",end="")
    i=i+1
print()

l=[10,20,30,40,50,60,70]
i=0
while i<len(l[0:5]):
    print(l[i])
    i=i+1
print()

#accessing elements from the list using for

l=[1,2,3,4,5]
for i in l:
    print(i)
print()

l=[1,2,3,4,5]
for i in l[0:3]:
    print(i)
print()

l=[1,2,3,4,5]
for i in l[::-1]:
    print(i)
print()



