
'''#case1--exception raised at outer try and corresponding except block is matched
try:
    print(int("abc"))#stat1
    try:
        print("inner try block")#stat2
        print("inner try block2")#stat3
    except ZeroDivisionError:
        print("inner except block")#stat4
    finally:
        print("inner finally block")#stat5
    print("outside the inner block")#stat6
except ValueError:
    print("outer except block")#stat7
    print("outer except block2")#stat8
finally:
    print("outer finally block")#stat9
print("outside the all block")#stat10
#output---7,8,9,10'''

'''#case2--exception raised at outer try and corresponding except block is not matched
try:
    print(int("abc"))#stat1
    try:
        print("inner try block")#stat2
        print("inner try block2")#stat3
    except ZeroDivisionError:
        print("inner except block")#stat4
    finally:
        print("inner finally block")#stat5
    print("outside the inner block")#stat6
except SyntaxError:
    print("outer except block")#stat7
    print("outer except block2")#stat8
finally:
    print("outer finally block")#stat9
print("outside the all block")#stat10
#output---9,valueerror'''

#case3--exception raised at inner try(stat3) and corresponding except block is  matched
try:
    print("hello")#stat1
    try:
        print("inner try block")#stat2
        print(10/0)#stat3
    except ZeroDivisionError:
        print("inner except block")#stat4
    finally:
        print("inner finally block")#stat5
    print("outside the inner block")#stat6
except SyntaxError:
    print("outer except block")#stat7
    print("outer except block2")#stat8
finally:
    print("outer finally block")#stat9
print("outside the all block")#stat10
#output---1,2,4,5,6,9,10