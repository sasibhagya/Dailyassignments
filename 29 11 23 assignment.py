#pro to print diff vowels present in the given word and count of vowels
name="we are learning python programming language"
a=name.count("a")
b=name.count("e")
c=name.count("i")
d=name.count("o")
e=name.count("u")
sum=0
list=[a,b,c,d,e]
for j in list:
    sum=sum+j
print("Total vowels in the given word are:",sum,"and those are :-",end="")

for i in name:
    if i in "aeiou":
        print("",i,"",end="",)
print()

#pr to enter the name and % of marks in a dict and display info on the screen
student_info = {}

num_students = int(input("Enter the number of students: "))

for i in range(num_students):
    name = input(f"Enter the name of student {i + 1}: ")
    percentage = float(input(f"Enter the percentage of marks for {name}: "))
    student_info[name] = percentage

print("\nStudent Information:")
for name, percentage in student_info.items():
    print(f"{name}: {percentage}%")


#write a pro to eliminate duplicates in the list
