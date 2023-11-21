
#2programmes to print +ve and -ve index of a string
'''
name="Iam learning python programming language"
word=0
for i in name:
    print("the positive index of a",i, "is",word,)
    word=word+1

print("")

name="Iam learning python programming language"
word=0
for i in name:
    print("the negative index of a",i, "is",word-len(name),)
    word=word+1
    '''
'''
#slicing 10 examples
name="Iam learning python programming language"
print(name[:])
print(name[0:9])
print(name[9:0])#blank
print(name[-1:-10])
print(name[-1:-11:-1])
print(name[9:-1])
print(name[9:-1:-1])#blank
print(name[9:-39])#blank
print(name[9:-39:-1])
print(name[::-1])'''

'''#5 examples on strip,lstrip,rstrip
name=input("enter the name: ")
for i in name.strip():  
    print(i)

list=["bhagya","sasi","dharani","rama","ramesh"]
name=input("enter the name:")
if name.strip() in list:
    print("hi",name,"is registered")
else:
    print(" your name is not in registered list")    

name="   \nbhgyasgd  "
print(name.strip())
    

name=input("enter the name:")
print(name.strip())

name="####iam learning  pytho#n programming language   "
print(name.strip("#"))'''

'''#5 examples of lstrip

name=input("enter the name: ")
for i in name.lstrip():  
    print(i)

list=["bhagya","sasi","dharani","rama","ramesh"]
name=input("enter the name:")
if name.lstrip() in list:
    print("hi",name,"is registered")
else:
    print(" your name is not in registered list")    

name="   \nbhgyasgd  "
print(name.lstrip())  
    

name=input("enter the name:")
print(name.lstrip())
  
name="####iam learning  pytho#n programming language ####  "
print(name.lstrip("#"))'''


'''#5 examples on rstrip

name=input("enter the name: ")
for i in name.rstrip():  
    print(i)

list=["bhagya","sasi","dharani","rama","ramesh"]
name=input("enter the name:")
if name.rstrip() in list:
    print("hi",name,"is registered")
else:
    print(" your name is not in registered list")    

name="   \nbhgyasgd  "
print(name.rstrip())  
    

name=input("enter the name:")
print(name.rstrip())
  
name="####iam learning  pytho#n programming language####"
print(name.rstrip("#"))

name="####iam learning  pytho#n programming language####   "
print(name.rstrip("#"))'''

#5 examples on find and rfind

'''name="python is a programming language and it is very simple"
print(name.find("P"))#case sensistive
print(name.find("is"))# found 1st is
print(name.find("b"))#not having b
print(name.find("p"))#1st p
print(name.find("lan"))#even print half word it is showing
print(name.find("a",0,20))
print(name.rfind("a",0,20))
print(name.rfind("is"))
print(name.rfind("P"))
print(name.rfind("a"))
print(name.rfind("mm"))
print(name.find("mm"))#in 116  and 117 both shows the same output'''

#5examples on index and rindex
'''
name="python is a programming language and it is very simple"
#print(name.index("P"))#case sensistive
print(name.index("is"))# found 1st is
#print(name.index("b"))#substring not found error
print(name.index("p"))#1st p
print(name.index("lan"))#even print half word it is showing
print(name.index("a",0,20))
print(name.rindex("a",0,20))
print(name.rindex("is"))
#print(name.rindex("P"))
print(name.rindex("a"))
print(name.rindex("mm"))
print(name.index("mm"))
print(name.rindex("mmm"))#substring notfound error
'''

#15/11/2023
#split function
#programme to reverse a string using split

'''s = "beast a is rangerover"
reversed_characters = ' '.join([word[::-1] for word in s.split()])
print(reversed_characters)'''

s="rangerover is a beast"
l=s.split()
for i in l[::-1]:
    print(i,"",end="")
print()

s="rangerover is a beast"
l=s.split()
for i in l[::-1]:
    print(i[::-1],"",end="")
print()

s="rangerover is a beast"
l=s.split()
for i in l:
    print(i[::-1],"",end="")
print()

#lower,upper,swapcase,capitalise,title 2examples each
#lower
name="BHAGYASREE"
print(name.lower())
name="BHAGyasree"
print(name.lower())

#upper
name="bhagyasree"
print(name.upper())
name="BHAGyasree"
print(name.upper())

#swapcase
name="BHAGyasree"
print(name.swapcase())
name="bhagyaSREE"
print(name.swapcase())

#capitalize
name="python training"
print(name.capitalize())
name="python coding training"
print(name.capitalize())

#title
name="python training"
print(name.title())
name="python coding training"
print(name.title())





