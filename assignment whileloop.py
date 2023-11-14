
# print 1st 10 numbers
i=1
while i<=10:
    print(i)
    i=i+1


#1st 20 numbers with skip value
i=1
while i<=20:
    print(i)
    i=i+2


#square the values
i=1
while i<=10:
    print(i*i)
    i=i+1


#print sum of 1st 10 numbers
i=1
sum=0
while i<=10:
    sum=sum+i
    i=i+1   
print(sum)


#sum of even numbers between 1 to 100
sum=0
i=2
while i<=100:
    sum+=i
    i=i+2
print(sum)



# factorial of given number
num=int(input("enter the value: "))
i=1
factorial=1
while i<=num:
    print(i)
    factorial*=i
    i=i+1
    
print(factorial)


#print a number in a table format 
n=int(input("enter the value: "))
i=1
while i<=10:
    print(n,'x',i,'=',n*i)
    i=i+1


#print stars in right angle triangle
i=1
while i<=10:
    print(i*'*')
    i=i+1


#print given string
name="bhagya"
i=0
while i<len(name):
    print(name[i],end="")
    i=i+1


 