#5 examples on del, clear,dict,len,get,pop,popitem,keys,values,items each

#del--to delete specific element in the dict based on keys
import asyncore


d={1:2,2:3,3:4,4:5}
del d[2]
print(d)

d={1:2,2:3,3:4,4:5,2:7}
del d[2]
print(d) #it will delete both the keys with 2

d=dict([(1,"ram"),(2,"sita"),(3,"sita"),(4,"laxman")])
del d[2]
print(d) 

'''d=dict([(1,"ram"),(2,"sita"),(3,"sita"),(4,"laxman")])
del d[5]
print(d) #key error :5

d={[(1,2),(2,3),(3,4),(4,5)]}
del d[2]
print(d) # type error  :  unhashable type :"list"

d={1:2,2:3,3:4,4:5}
del(d[1,2])
print(d) # key error 

d=dict([(1,"ram"),(2,"sita"),(3,"sita"),(4,"laxman")])
del d["ram"]
print(d) # key error'''


#clear - to clear all the elements in the dict
d={1:2,2:3,3:4,4:5}
d.clear()
print(d)

d={}
d.clear()
print(d)

d={}
d.clear()
d[1]="ram"
print(d)

d={}
d[1]="ram"
d.clear()
print(d)

#dict()

d=dict([[1,"ram"],[2,"sita"],[3,"sita"],[4,"laxman"]])
print(d)

d=dict(([1,"ram"],[2,"sita"],[3,"sita"],[4,"laxman"]))
print(d) 

'''d=dict({[1,"ram"],[2,"sita"],[3,"sita"],[4,"laxman"]})
print(d) # type error'''


d=dict([(1,"ram"),(2,"sita"),(3,"sita"),(4,"laxman")])
print(d)

d=dict(((1,"ram"),(2,"sita"),(3,"sita"),(4,"laxman")))
print(d) 

d=dict({(1,"ram"),(2,"sita"),(3,"sita"),(4,"laxman")})
print(d) 


d=dict([{1,"ram"},{2,"sita"},{3,"sita"},{4,"laxman"}])
print(d)

d=dict(({1,"ram"},{2,"sita"},{3,"sita"},{4,"laxman"}))
print(d)

'''d=dict({{1,"ram"},{2,"sita"},{3,"sita"},{4,"laxman"}})
print(d) #type error'''

#len - to count length of the dict

d=dict([(1,"ram"),(2,"sita"),(3,"sita"),(4,"laxman")])
print(len(d))

d=dict()
print(len(d))

#get - to get specific element based on keys if specific element is not present it shows none

d=dict([(1,"ram"),(2,"sita"),(3,"sita"),(4,"laxman")])
print(d.get(2) )

d=dict([(1,"ram"),(2,"sita"),(3,"sita"),(4,"laxman")])
print(d.get(2,3) )

d=dict([(1,"ram"),(2,"sita"),(3,"sita"),(4,"laxman")])
print(d.get(5,3) )

d=dict([(1,"ram"),(2,"sita"),(3,"sita"),(4,"laxman")])
print(d.get(5))

d=dict()
print(d.get(5,3))

d=dict()
print(d.get(5))

#pop-to return specific element from the dict and we should pass one argument


d=dict([(1,"ram"),(2,"sita"),(3,"sita"),(4,"laxman")])
print(d.pop(2))

d=dict([(1,"ram"),(2,"sita"),(3,"sita"),(4,"laxman")])
print(d.pop(2,3))

d=dict([(1,"ram"),(2,"sita"),(3,"sita"),(4,"laxman")])
print(d.pop(5,3))

'''d=dict([(1,"ram"),(2,"sita"),(3,"sita"),(4,"laxman")])
print(d.pop(5)) #key error :5

d=dict()
print(d.pop(5)) #key error :5

d=dict([(1,"ram"),(2,"sita"),(3,"sita"),(4,"laxman")])
print(d.pop()) # type error '''

d=dict()
print(d.pop(5,3))

#popitem--to return top of the element along with key from the dict and should not pass the argument

d=dict([(1,"ram"),(2,"sita"),(3,"sita"),(4,"laxman")])
print(d.popitem())

'''d=dict()
print(d.popitem()) # key error : dictionary is empty

d=dict([(1,"ram"),(2,"sita"),(3,"sita"),(4,"laxman")])
print(d.popitem(2)) #type error'''

#keys- to display all the keys from the dict

d=dict([(1,"ram"),(2,"sita"),(3,"sita"),(4,"laxman")])
print(d.keys())

d=dict([(1,"ram"),(2,"sita"),(2,"geetha"),(4,"laxman")])
print(d.keys())

d=dict()
print(d.keys()) # it prints empty dict not an error

#values - to display all the values from the dict

d=dict([(1,"ram"),(2,"sita"),(3,"sita"),(4,"laxman")])
print(d.values())

d=dict([(1,"ram"),(2,"sita"),(2,"geetha"),(4,"laxman")])
print(d.values()) # it prints updated value of 2

d=dict()
print(d.values())

d=dict([(1,"ram"),(2,"sita"),(2,"geetha"),(4,"laxman"),(1,"bhagya")])
print(d.values())


#items -- to display all the keys and 

d=dict([(1,"ram"),(2,"sita"),(3,"sita"),(4,"laxman")])
print(d)

d=dict([(1,"ram"),(2,"sita"),(3,"sita"),(4,"laxman")])
print(d.items())

d=dict([(1,"ram"),(2,"sita"),(2,"geetha"),(4,"laxman")])
print(d.items())

d=dict()
print(d.items())

#some examples
a=[1,2,3,4,5]
d={100:a}
print(d)

d=dict([(1,"ram"),(2,"sita"),(3,"geetha"),(4,"laxman")])
a=d.keys()
b=d.values()
for x in a:
    print("keys are",x)
for y in b:
    print("and the values are :",y)

d=dict([(1,"ram"),(2,"sita"),(3,"geetha"),(4,"laxman")])
a=d.keys()
b=d.values()
for x in a:
    print(x,end=", ")
print("are the keys and",end=" ")
for y in b:
    print(y,end=", ")
print("are the values")





