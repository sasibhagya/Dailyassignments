a=2
b=6
print(a+b) #answer :8
print(a-b) #answer :-4
print(a*b) #answer :12
print(a/b) #answer :0.3333333333333333
print(a**b) #answer :64
print(a//b)# answer :0
print(a%b) #answer :2

a=10.5
b=5.6
print(a+b) #answer :16.1
print(a-b) #answer :4.9
print(a*b) #answer :58.8
print(a/b) #answer :1.8750000000000002
print(a**b) #answer :523190.77135154256
print(a//b) #answer :1.0
print(a%b) #answer :4.9

a="bhagya"
b="sree"
print(a+b) #answer :bhagyasree
#print(a-b)---TypeError: unsupported operand type(s) for -: 'str' and 'str'
#print(a*b)---TypeError: can't multiply sequence by non-int of type 'str'
#print(a/b)---TypeError: unsupported operand type(s) for /: 'str' and 'str'
#print(a**b)---TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'str'
#print(a//b)---TypeError: unsupported operand type(s) for //: 'str' and 'str'
#print(a%b)---TypeError: not all arguments converted during string formatting

a=True
b=False
print(a+b) #answer :1
print(a-b) #answer :1
print(a*b) #answer :0
#print(a/b)---ZeroDivisionError: division by zero
print(a**b) #answer :1
#print(a//b)---ZeroDivisionError: integer division or modulo by zero
#print(a%b)---ZeroDivisionError: integer modulo by zero

a=2
b=5.6
print(a+b) #answer :7.6
print(a-b) #answer :-3.5999999999999996
print(a*b) #answer :11.2
print(a/b) #answer :0.35714285714285715
print(a**b) #answer :48.50293012833273
print(a//b)# answer :0.0
print(a%b) #answer :2.0

a=2
b="sree"
#print(a+b)---TypeError: unsupported operand type(s) for +: 'int' and 'str'
#print(a-b)---TypeError: unsupported operand type(s) for -: 'int' and 'str'
print(a*b) #answer :sreesree
#print(a/b)---TypeError: unsupported operand type(s) for /: 'int' and 'str'
#print(a**b)---TypeError: unsupported operand type(s) for ** or pow(): 'int' and 'str'
#print(a//b)---TypeError: unsupported operand type(s) for //: 'int' and 'str'
#print(a%b)---TypeError: unsupported operand type(s) for %: 'int' and 'str'

a=2
b=False
print(a+b) #answer :2
print(a-b) #answer :2
print(a*b) #answer :0
#print(a/b)---ZeroDivisionError: division by zero
print(a**b) #answer :1
#print(a//b)---ZeroDivisionError: integer division or modulo by zero
#print(a%b)---ZeroDivisionError: integer modulo by zero


a=10.5
b="sree"
#print(a+b)---TypeError: unsupported operand type(s) for +: 'float' and 'str'
#print(a-b)---TypeError: unsupported operand type(s) for -: 'float' and 'str'
#print(a*b)---TypeError: can't multiply sequence by non-int of type 'float'
#print(a/b)---TypeError: unsupported operand type(s) for /: 'float' and 'str'
#print(a**b)---TypeError: unsupported operand type(s) for ** or pow(): 'float' and 'str'
#print(a//b)---TypeError: unsupported operand type(s) for //: 'float' and 'str'
#print(a%b)---TypeError: unsupported operand type(s) for %: 'float' and 'str'

a=10.5
b=False
print(a+b) #answer :10.5

print(a-b) #answer :10.5
print(a*b) #answer :0.0
#print(a/b)---ZeroDivisionError: float division by zero
print(a**b) #answer :1.0
#print(a//b)---ZeroDivisionError: float floor division by zero
#print(a%b)---ZeroDivisionError: float modulo



a="bhagya"
b=False
#print(a+b)---TypeError: can only concatenate str (not "bool") to str
#print(a-b)---TypeError: unsupported operand type(s) for -: 'str' and 'bool'
print(a*b) #answer : empty
#print(a/b)---TypeError: unsupported operand type(s) for /: 'str' and 'bool'
#print(a**b)---TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'bool'
#print(a//b)---TypeError: unsupported operand type(s) for //: 'str' and 'bool'
#print(a%b)---TypeError: not all arguments converted during string formatting


