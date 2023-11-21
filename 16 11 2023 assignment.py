#1 reverse the user entered string
'''s=input("enter the string:")
l=s.split()
for i in l[::-1]:
    print(i,"",end="")

#2 remove duplicates from the input
name=input("enter the name:")
l=[]
for i in name:
    if i!=l:
        l.append(i)
r="".join(l)
print(r) ''' 

#accessing elements from nested list
l=[1,2,3,4,[5,6,7],8,9]
print(l[3],l[4][0])
print(l[4][2],l[5])


#2examples for split function

l="my name is bhagya"
m=l.split()
print(m)#result in list format
for i in m:
    print(i,"",end="")# result in string format
print()

l="iam learning python course"
m=l.split()
for i in m[1:3]:
    print(i,"",end="")#accessing learning python from the string
print()

#2examples for empty list

l=[]
for i in range(11):
    l.append(i)
print(l)

l=[]
for i in range(21):
    if i%2==0:
        l.append(i)
print(l)

l=[]
s=[1,2,3,4,5]
for i in s:
    l.append(i)
print(l)


'''
all string functions:
lower()---to convert upper charcters into lower
upper()---to convert lower characters to upper
swapcase()----to convert lower to upper and upper to lower 
capitalize()--to convert 1st character into upper
title()---to conver all 1st characters into upper
startswith()---to check whether the string starts with particular character/word or not
endswith()----to check whether the string ends with particular character/word or not
find()---to find the specific element is present or not....if not it will givr -1 as an output
index()---to find the specific element is present or not....if not it will givr error as an output
count()---to count how many times particular element is present in a given string(it is case sensitive)
replace()---to replace the element in a string with some other element
split()----to split the string based on spaces
strip()----to remove left side and right side spaces of a string
rstrip()---only to remove right side spaces
lstrip()---only to remove left side spaces
len()----to find the lenght of a string
join()---to join/add an extra character into the given string
isalpha()--to check the given string is with alphabets or not
isdigit()--to check the given string is with digits or not
isalnum()--to check the given string is with alphabets and digits or not
islower()---to check the given string is with lower case characters or not 
isupper()---to check the given string is with upper case characters or not 
istitle()---to check every 1st character of string is in upper case or not
isspace()---to check string is only with spaces or not
'''