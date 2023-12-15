# 5 examples of recursive , lambda, map, filter, reduce functions on each

#lambda

a=lambda n:n*n
print(a(3))

a=lambda n:n*5
print(a(5))

a=lambda n:n+n
print(a(3))


a=lambda a:"even" if a%2==0 else "odd"
print(a(4))
print(a(3))
print()

a=lambda n:"positive" if n>=0 else "negative"
print(a(5))
print(a(-1))
print()

#map

l=[1,2,3,4,5]
l1=[2,3,4,5,6]
a=map(lambda l,l1:l*l1,l,l1)
print(list(a))


l=[1,2,3,4,5]
l1=[2,3,4,5,6]
def m(l,l1):
    return l*l1
a=map(m,l,l1)
print(list(a))


l=[1,2,3,4,5]
def m(l):
    return l*l
a=map(m,l)
print(list(a))

l=[1,2,3,4,5,6,7,8,9,10]
def m(l):
    if l%2==0:
        return l            
a=map(m,l)
print(list(a))

l=[1,2,3,4,5]
def m(l):
    return l*2
a=map(m,l)
print(list(a))


#filter

l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
def m(l):
    if l%2==0:
        return l            
a=filter(m,l)
print(list(a))

l=[1,2,-3,4,-5,6,-7,8,9,-10,11,12,13,14,15,-16,17,18,19,20]
def m(l):
    if l>=0:
        return l            
a=filter(m,l)
print(list(a))

name="bhagyasree is a very good girl"
def m(name):
    if name=="a":
        return name           
a=filter(m,name)
print(list(a))

# function to filter int data type from mixed datatypes
def m(l):
    return isinstance(l,int)
l=[1,2,-3,11,12.5,13,14,15,-16,17,18.2,True,"bhagya"]                
a=filter(m,l)
print(list(a))  #here boolean is not removed because here true is considered as integer "1"

l=[1,2,-3,11,12.5,13,14,15,-16,17,18.2,True,"bhagya"]
a=filter(lambda l:isinstance(l,int),l)
print(list(a))


#reduce

from functools import *
l=[1,2,3,4,5,6,7,8,9]
def m(a,b):
   return a*b         
x=reduce(m,l)
print(x)

from functools import *
l=[1,2,3,4,5,6,7,8,9]
def m(a,b):
   return a+b         
x=reduce(m,l)
print(x)


from functools import *
l=[9,8,7,6,5,4,3,2,1]
def m(a,b):
   return a-b         
x=reduce(m,l)
print(x)


#recursion

def fac(n):
    if n==0:
        return 1
    else:
        return n*fac(n-1)
x=fac(6)

print(x)

def fac(n):
    if n==0:
        return 1
    else:
        return n+fac(n-1)
x=fac(6)
print(x)