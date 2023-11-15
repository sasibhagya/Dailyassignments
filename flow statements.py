'''#1st pronlem

a=int(input("enter a value: "))
b=int(input("enter b value: "))

if a>b:
    print("a is the greater number:" , a)
elif b>a:
    print("b is the greater number: ", b)
else:
    print("both numbers are same")



#2nd problem
a=int(input("enter the value: "))
if a<=100:
    print("your number is in between 1 to 100")
else:
    print("you are out of range")





#3rd problem
a=int(input("enter the value: "))
if a==1:
    print("one")
elif a==2:
    print("two")
elif a==3:
    print("three")
elif a==4:
    print("four")
elif a==5:
    print("five")
elif a==6:
    print("six")
elif a==7:
    print("seven")
elif a==8:
    print("eight")
elif a==9:
    print("nine")
else:
    print("you have entered 2 digit number")




name=input("enter your name : ")
if name=="Bhagya" or name=="bhagya":
    print("yes , you are in python class")
elif name=="sasi" or name=="Sasi":
    print("yes , you are in python class")
elif name=="Dharani" or name=="dharani":
    print("yes , you are in python class")
else:
    print("your name is not registered in python class")


'''
    
'''#06/11/2023
name=""
password=""

while name!="bhagya" or password!=1234:
    name=input("enter your name to verify: ")
    password=int(input("enter your password :"))
print("hello",name,"you entered the correct password:",password)'''


#15/11/2023
#programme to display all the positions of substring in the given string

s=input("enter the string:")
subs=input("enter the value:")
f=False
position=-1
n=len(s)
while True:
    position=s.find(subs,position+1,n)
    if position ==-1:
        break
    print("found at index:",position)
    f=True
if f==False:
    print("not found")
