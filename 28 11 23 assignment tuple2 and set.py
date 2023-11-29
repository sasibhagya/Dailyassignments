#write a pro to take tuple of numbers from keyboard and print Sum,avg
t=(10,20,30,40,50)
sum=0
for i in t:
    sum=sum+i
print(sum)

t=(10,20,30,40,50,60)
sum=0
avg=len(t)
for i in t:
    sum=sum+i
print(sum/avg)

#set
# 5 examples on add,update,pop,remove,discard,copy
# add   
# 
# s={10,20,30,40}
s.add(60)
print(s)

'''s={10,20,30,40}
s.add(60,50)
print(s)'''

'''s={}
s.add(60)
print(s) #attribute error'''

s=set()
s.add(60)
print(s)

s={10,20,30,40}
s2=set()
s.add(60)
for s2 in s:
    pass
print(s)

#update
s={10,20,30,40,50}
b=(50,60,70)
s.update(b)
print(s)

s={10,20,30,40,50}
b=s.update([50,60,70])
print(b)

s={10,20,30,40,50}
b=(50,60,70,"aman")
s.update(b)
print(s)

'''s={10,20,30,40,50}
s.update(50,60,70)
print(s) #type error'''


s={10,20,30,40,50}
b={100,200,300}
s.update(b,range(1,20))
print(s)

s={10,20,30,40,50}
s.update(range(1,20))
print(s)

#copy

s={10,20,30,40,50}
b=s.copy()
print(b)

s={10,20,30,40,50,50,10}
b=s.copy()
print(b)

s={10,20,30,40,50}
a=[10,20,30,40,50]
b=s,a.copy()
print(b)

s={10,20,30,40,50}
a=[]
b=s,a.copy()
print(b)

s={10,20,30,40,50}
a={10,20,30,40,50}
b=s,a.copy()
print(b)

s={10,20,"bhagya",10.6,True}
a=s.copy()
print(a)

'''s={10,20,30,{70,1,2,3},40,50}
a=s.copy()
print(a) #type error'''

#pop

s={10,20,30,40}
s.pop()
print(s)

s={10,20,30,40}
s.pop()
s.pop()
print(s)

s={10,20,30,40}
b=s.pop()
print(b)

'''s={10,20,30,40}
b=s.pop(2)
print(b) #type error'''

s={10,20,"bhagya",10.6,True}
s.pop()
print(s)
s.pop()
print(s)
s.pop()
print(s)
s.pop()
print(s)
s.pop()
print(s)

'''s=set()
s.pop()
print(s)#key error'''

#remove

s={10,20,30,40,50}
s.remove(30)
print(s)

'''s={10,20,30,40,50}
s.remove(70)
print(s) #key error'''

'''s=set()
s.remove()
print(s)# type error'''

'''s=set()
s.remove(30)
print(s)#key error'''

s={10,20,"bhagya",10.6,True}
s.remove("bhagya")
print(s)

'''s={10,20,30,40,50}
s.remove(30,40)
print(s)#type error'''
 