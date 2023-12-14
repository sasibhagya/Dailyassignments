# pro to print sum if given number in var len argu

def add(*x):
    sum=0
    for i in x:
        sum=sum+i
        i=i+1
    print(sum)
add(10,20,30,40,50)


#10-15 possible scenerions on the \below programme
def f(arg1,arg2,arg3=4,arg4=8):
    print(arg1,arg2,arg3,arg4) 
f(3,5)
f(10,20,30,40)
f(11,6,arg4=1000)
f(arg4=6,arg1=7,arg2=9)
# f(arg3=90,arg4=80,10,50)    SyntaxError: positional argument follows keyword argument
#f(6,8,arg2=89)  got multiple values arg2
#f(4,5,arg3=7,arg5=78)  TypeError: f() got an unexpected keyword argument 'arg5' 
#f()   missing 2 required positional arguments: 'arg1' and 'arg2'
