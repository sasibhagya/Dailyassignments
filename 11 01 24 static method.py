
#static variable inside the class
#1
class Bhagya:
    a=10
Bhagya()
print(Bhagya.a)
print()

#2
class Bhagya:
    a=10
print(Bhagya.a)
print()

#inside the constructor
#3
class Bhagya:
    def __init__(self):
        Bhagya.a=20
Bhagya()
print(Bhagya.a)
print()

'''class Bhagya:
    def __init__(self):
        Bhagya.a=20
print(Bhagya.a) #error'''

#4
class Bhagya:
    a=30
    def __init__(self):
        print(Bhagya.a)
Bhagya()
print()

#inside the instance method
#5
class Bhagya:
    a=40
    def abc(self):
        print(Bhagya.a)
        Bhagya.b=90
b=Bhagya()
b.abc()
print(Bhagya.b)
print()

#inside the class method
class Bhagya:
    a=40
    def __init__(self) -> None:
        pass
    @classmethod
    def xyz(cls):
        print(Bhagya.a)
        Bhagya.d=600
        cls.c=900
b=Bhagya()
b.xyz()
print(b.d)
print(b.c)
print()

#inside the static method
class Bhagya:
    a=40
    def __init__(self) -> None:
        pass
    @classmethod
    def xyz(cls):
        print(Bhagya.a)
        Bhagya.d=600
        cls.c=900
    @staticmethod
    def abc():
        Bhagya.t=1200
b=Bhagya()
b.abc()
b.x=20#outside the class
print(b.t)
print(b.x)
print()

#some examples
#1
class school:
    a=20
    def __init__(self) -> None:
        school.b=30
        self.x=900
    def exam(self):
        school.c=70
        self.u=1000
    @classmethod
    def abc(cls):
        cls.d=800
    @staticmethod
    def xyz():
        school.e=600
print(school.__dict__) #print only 20


#2
class school:
    a=20
    def __init__(self) -> None:
        school.b=30
        self.x=900
    def exam(self):
        school.c=70
        self.u=1000
    @classmethod
    def abc(cls):
        cls.d=800
    @staticmethod
    def xyz():
        school.e=600
s=school()
s.exam()
s.abc()
s.xyz()
print(school.__dict__)#print all static variables


#3
class school:
    a=20
    def __init__(self) -> None:
        school.b=30
        self.x=900
    def exam(self):
        school.c=70
        self.u=1000
    @classmethod
    def abc(cls):
        cls.d=800
    @staticmethod
    def xyz():
        school.e=600
s=school()
s.exam()
s.abc()
s.xyz()
print(s.__dict__)#print only instance variables


#4
class school:
    a=20
    def __init__(self) -> None:
        school.b=30
        self.x=900
    def exam(self):
        school.c=70
        self.u=1000
    @classmethod
    def abc(cls):
        cls.d=800
    @staticmethod
    def xyz():
        school.e=600
s=school()
s.abc()
s.xyz()
print(s.__dict__) # only 900 because we are not calling exam method


#5
class school:
    a=20
    def __init__(self) -> None:
        school.b=30
        self.x=900
    def exam(self):
        school.c=70
        self.u=1000
    @classmethod
    def abc(cls):
        cls.d=800
    @staticmethod
    def xyz():
        school.e=600
s=school()
s.abc()
s.exam()
s.z=1100# instance variable
s.xyz()
print(s.__dict__)# all instance variables

#6
class school:
    a=20
    def __init__(self) -> None:
        school.b=30
        self.x=900
    def exam(self):
        school.c=70
        self.u=1000
    @classmethod
    def abc(cls):
        cls.d=800
    @staticmethod
    def xyz():
        school.e=600
s=school()
s.abc()
s.exam()
school.z=1100#static variable
s.xyz()
print(school.__dict__)

#7
class school:
    a=20
    def __init__(self) -> None:
        school.b=30
        self.x=900
    def exam(self):
        school.c=70
        self.u=1000
    @classmethod
    def abc(cls):
        cls.d=800
    @staticmethod
    def xyz():
        school.e=600
s=school()
s.abc()
s.exam()
s.z=1100#instance variable
s.xyz()
print(school.__dict__)