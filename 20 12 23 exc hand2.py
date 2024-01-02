
#case1--exception raised at outer try and corresponding except block is matched
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
#output---7,8,9,10

#case2--exception raised at outer try and corresponding except block is not matched
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
#output---9,valueerror

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

#case4--exception raised at inner try(stat3) and corresponding except block is not matched
try:
    print("hello")#stat1
    try:
        print("inner try block")#stat2
        print(10/0)#stat3
    except ValueError:
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
#output---1,2,4,9,Zero division error

#case5--exception raised at inner try(stat3) and corresponding except block is not matched but outer except block is matched
try:
    print("hello")#stat1
    try:
        print("inner try block")#stat2
        print(10/0)#stat3
    except ValueError:
        print("inner except block")#stat4
    finally:
        print("inner finally block")#stat5
    print("outside the inner block")#stat6
except ZeroDivisionError:
    print("outer except block")#stat7
    print("outer except block2")#stat8
finally:
    print("outer finally block")#stat9
print("outside the all block")#stat10
#output---1,2,5,7,8,9,10

#case6--exception raised at outer try(stat1) and corresponding except block is  matched but also exception raised at inner except block
try:
    print(10/0)#stat1
    try:
        print("inner try block")#stat2
        print("inner try block2")#stat3
    except ZeroDivisionError:
        print(10/0)#stat4
    finally:
        print("inner finally block")#stat5
    print("outside the inner block")#stat6
except ZeroDivisionError:
    print("outer except block")#stat7
    print("outer except block2")#stat8
finally:
    print("outer finally block")#stat9
print("outside the all block")#stat10
#output---7,8,9,10

#case7--exception raised at outer try(stat1) and corresponding except block is not matched and also exception raised at inner except block
try:
    print(10/0)#stat1
    try:
        print("inner try block")#stat2
        print(10/0)#stat3
    except ZeroDivisionError:
        print(10/0)#stat4
    finally:
        print("inner finally block")#stat5
    print("outside the inner block")#stat6
except SyntaxError:
    print("outer except block")#stat7
    print("outer except block2")#stat8
finally:
    print("outer finally block")#stat9
print("outside the all block")#stat10
#output---9,zero division error

#case8--exception raised at inner try(stat3) and corresponding except block is  matched and also exception raised at inner except block
try:
    print("outer try")#stat1
    try:
        print("inner try block")#stat2
        print(10/0)#stat3
    except ZeroDivisionError:
        print(10/0)#stat4
    finally:
        print("inner finally block")#stat5
    print("outside the inner block")#stat6
except SyntaxError:
    print("outer except block")#stat7
    print("outer except block2")#stat8
finally:
    print("outer finally block")#stat9
print("outside the all block")#stat10
#output---1,2,5,9,zero division error

#case9--exception raised at inner try(stat3) and corresponding except block is not matched and also exception raised at inner except block
try:
    print("outer try")#stat1
    try:
        print("inner try block")#stat2
        print(10/0)#stat3
    except TypeError:
        print(10/0)#stat4
    finally:
        print("inner finally block")#stat5
    print("outside the inner block")#stat6
except SyntaxError:
    print("outer except block")#stat7
    print("outer except block2")#stat8
finally:
    print("outer finally block")#stat9
print("outside the all block")#stat10
#output---1,2,5,9,zero division error

#case10--exception raised at  inner finally block(stat5)
try:
    print("outer try block")#stat1
    try:
        print("inner try block")#stat2
        print("inner try block2")#stat3
    except ZeroDivisionError:
        print("inner except block")#stat4
    finally:
        print(10+"abc")#stat5
    print("outside the inner block")#stat6
except SyntaxError:
    print("outer except block")#stat7
    print("outer except block2")#stat8
finally:
    print("outer finally block")#stat9
print("outside the all block")#stat10
#output---1,2,3,9,type error

#case11--exception raised at outer try(stat1) and corresponding except block is  matched and also exception raised at outer except block
try:
    print(10/0)#stat1
    try:
        print("inner try block")#stat2
        print("inner try block2")#stat3
    except ZeroDivisionError:
        print("inner except block")#stat4
    finally:
        print("inner finally block")#stat5
    print("outside the inner block")#stat6
except ZeroDivisionError:
    print(10+"abc")#stat7
    print("outer except block2")#stat8
finally:
    print("outer finally block")#stat9
print("outside the all block")#stat10
#output---9,zero division error

#case12--exception raised at outer try(stat1) and corresponding except block is not matched and also exception raised at outer except block
try:
    print(10/0)#stat1
    try:
        print("inner try block")#stat2
        print("inner try block2")#stat3
    except ZeroDivisionError:
        print("inner except block")#stat4
    finally:
        print("inner finally block")#stat5
    print("outside the inner block")#stat6
except SyntaxError:
    print(10+"abc")#stat7
    print("outer except block2")#stat8
finally:
    print("outer finally block")#stat9
print("outside the all block")#stat10
#output---9,zero division error
