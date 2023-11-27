#write a program to display unique vowels present in the given words
word="my name is bhagya iam learning python course in marolix solutions"
for i in word:
    if i in "aeiou":
        print(i,"",end="")
print()

# multiply the tuple with 2
l=(10,20,30,40,50)
print(l*2)

#types of tuple we can write
t=(10,20,30,40)
print(type(t))

t=10,20,30,40
print(type(t))

t=10
print(type(t))

t=10,
print(type(t))

t=()
print(type(t))

t=(10)
print(type(t))

t=(10,)
print(type(t))
