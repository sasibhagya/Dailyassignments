#using class method decorator
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    @classmethod
    def create_from_str(cls, string):
        x, y = map(int, string.split(","))
        return cls(x, y)
obj1 = MyClass.create_from_str("4,6")
print(obj1.x)  
print(obj1.y) 


#2
class abc:
    def __init__(self, x, y):
        self.x = y
        self.y = y

    @classmethod
    def display(cls, num):
        return cls(num,num)
a = abc.display(5)
print(a.x)  
print(a.y) 


#without using decorator
class MyClass:
    def __init__(self, abc):
        x, y = map(int, abc.split(","))
        self.x = x
        self.y = y
    
    def display(self):
        print(self.x)
        print(self.y)
obj3 = MyClass("2,8")
obj3.display()

class abc:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self, num):
        return abc(num, num)
obj1 = abc.display(5,6)
print(obj1.x)  
print(obj1.y)


#without using decorator and accesing values from one method to another method
class MyClass:
    def __init__(self, abc):
        self.abc = abc
    
    def create(self):
        x, y = map(int, self.abc.split(","))
        self.x = x
        self.y = y
    
    def display(self):
        print(self.x)
        print(self.y)
obj2 = MyClass("3,5")
obj2.create()
obj2.display()