
# print 1st 10 numbers
for i in range(1,11):
    print(i)

#1st 20 numbers with skip value
for i in range(1,21,2):
    print(i)

#square the values
for i in range(1,11):
    print(i*i)


#print sum of 1st 10 numbers
sum=0
for i in range(1,11):
    sum=sum+i
    print(i)   
print(sum)

#sum of even numbers between 1 to 100
sum=0
for i in range(1,101):
    if i%2==0:
        print(i)
        sum+=i
print(sum)

# factorial of given number
num=int(input("enter the value: "))
count=1
for i in range(1,num+1):
    print(i)
    count*=i
print(count)


#print a number in a table format 
n=int(input("enter the value: "))
for i in range(1,11):
    print(n,'x',i,'=',n*i)


#print stars in right angle triangle
for i in range(1,11):
    print(i*'*')


#print given string
name="bhagya"
for i in name:
    print(i,end="")


 #reverse a string
name="bhagya"
for i in name[::-1]:
    print(i)


#whether the values in a sequese are positive or not
a=[-1,2,3,-4,5,6,-7,8,-9,10,56,-40]
for i in a:
    if i>=0:
        print("positive number")
    else:
        print("negative number")


#print  string with index number
count=0
name=input("enter the name: ")
for i in name:
    print(count,i)
    count=count+1


#print alternate charcters of string 
name="bhagyasree"
for i in name[0:10:2]:
    print(i)

#average of elements in a list
n=[10,20,30,40,50]
sum=0
count=0
for i in n:
    sum=sum+i
    count+= 1
    average=sum/count
print("The average of the numbers is:", average)


# common elements between 2 lists
l1=[10,40,32,29,47,92,20,30]
l2=[10,20,30,40,34,82,46,15]

for i in l1:
   for i2 in l2:
     if i==i2:
         print(i)


#remove duplicate elements    
n= [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
list=[]
for i in n:
    if i not in list:
        list.append(i)
print(list)  


#whether the string is palindrome or not
name="bhagya"
rname=name[::-1]
for i in name:
    if i==rname:
        print("not a palindrome")
else:
    print("palindrome")


#sum of all the elements in a list
l1=[10,20,30,40,50]
sum=0
for i in l1:
    sum=sum+i
print(sum)


#sum of even numbers in a list
n=[1,2,3,4,5,6,7,8,9]
sum=0
for i in n:
    if i%2==0:
        sum+=i
print(sum) 


#sum of odd numbers in a list
n=[1,2,3,4,5,6,7,8,9]
sum=0
for i in n:
    if i%2!=0:
        sum+=i
print(sum) 
