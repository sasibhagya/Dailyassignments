# 20 examples on functions

#1 adding 2 numbers using print
def add(num1,num2):
    print(num1+num2)
add(10,20)

#2 adding 2 numbers using return
def add(num1,num2):
    return num1+num2
x=add(10,20)
print(x)

#3 printing the calling value
def number(n):
        print(n)
number(10)


#4 sum of first 20 even numbers
def number():
    sum=0
    for i in range(1,21):
        if i%2==0:
            sum=sum+i
            i=i+1
    print(sum)
number()

#5 pro to find the factorial of given function

def fac(n):
    a=1
    while n>=1:
        a=a*n
        n=n-1
    return a
print(fac(5))

#6 Create a function that calculates the square root of a given number

def sq(n):
    print(n*n)
sq(5)

#7 Write a function to reverse a string

def rev(name):
    for i in name[::-1]:
        print(i,end=" ")
rev("bhagya")
print()

#8 function to check if a string is a palindrome

name="bhagya"
rname=name[::-1]
def pal():
    if name==rname:
        print("not a palindrome")
    else:
        print("palindrome")
pal()

#9 function that counts the number of vowels in a given string
def count(name):
    a=name.count("a")
    b=name.count("e")
    c=name.count("i")
    d=name.count("o")
    e=name.count("u")
    list=[a,b,c,d,e]
    sum=0
    for i in list:
        sum=sum+i
    print("Number of vowels:",sum)
count("my name is bhagya sree and iam learning python programming language")

# 10  function to check if a number is even or odd.

def num(n):
    if n%2==0:
        print("even")
    else:print("odd")
num(11)

#11  function that takes a list of numbers and returns a new list with only the even numbers

def even():
    l=[1,2,3,4,5,6,7,8,9,10]
    l1=[]
    for i in l:
        if i%2==0:
            l1.append(i)
    print(l1)
even()

#12  function to find the second largest element in a list.

l=[12,34,56,11,43,58,67]
def num():
    largest_number=max(l)
    l.remove(largest_number)
    second_largest=max(l)
    print(second_largest) 
num()

#13 function that removes duplicates from a list

l=[1,2,3,45,1,34,23,3,89,56,34,3,1,2]
def num():
    a=set(l)
    b=list(a)
    print(b)
num()

#14 function to reverse the order of elements in a list

l=[12,34,56,11,43,58,67]
def rev():
    l.reverse()
    print(l)
rev()

#15 function that accepts a sentence and returns the number of words in it

name="my name is bhagya sree and iam learning python programming language"
def words():
    a=name.count(" ")
    print(a+1)
words()

#16 function to calculate the average of elements in a list

def average():
    l=[1,2,3,4,5,6]
    sum=0
    avg=len(l)
    for i in l:
        sum=sum+i
        i=i+1
    print(sum/avg)
average()



