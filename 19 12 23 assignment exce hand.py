#exception handling

# case-1----if there is no error in try block statement---NT
'''try:
    print("hello")
    print("10/2")
    print("good morning")
except:
    print("error occured")
print("bhagya") #output---1,2,3,5'''

#case-2 ----if an excep raised at stat-2 and corresponding except block is matched ---NT
'''try:
    print("hello")
    print("10"+12)
    print("good morning")
except TypeError:
    print("error occured")
print("bhagya") #output---1,4,5'''

#case -3----if an excep raised at stat-2 and corresponding except block is not matched---ABT
'''try:
    print("hello")
    print("10"+12)
    print("good morning")
except ValueError:
    print("error occured")
print("bhagya")#output---1,typeerror'''

#case-4 ----if an excep raised at stat-2 and corresponding except block is matched and also Exception raised in except block---ABT
'''try:
    print("hello")
    print("10"+12)
    print("good morning")
except TypeError:
    print(10/0)
print("bhagya")#output---1,typeerror,zerodivisionerror'''


#case-5 ----if an excep raised at stat-2 and corresponding except block is not matched and also Exception raised in except block---ABT
'''try:
    print("hello")
    print("10"+12)
    print("good morning")
except ZeroDivisionError:
    print(10/0)
print("bhagya")#output---1,typeerror'''

# case-6----if there is no error in try block statement and exception raised at statement5
'''try:
    print("hello")
    print(10+12)
    print("good morning")
except ZeroDivisionError:
    print("error occured")
print(10/0)# output----1,2,3,zerodivisionerror'''

#Example for syntax error
'''try:
    print("hello")
except SyntaxError as m
    print("error occured")
print("bhagya") #output ---syntaxerror:expected ':','''