#1 using object reference
class studentdata():
    clg="narayana"
    def __init__(self,name,rollno,age,section):
        self.name=name
        self.rollno=rollno
        self.age=age
        self.section=section
    def progress(self):
        print(self.clg,self.name,self.rollno,self.age,self.section)
a=studentdata("bhagya",33,25,"A")
a.progress()
studentdata("bhagya",33,25,"A").progress()
print()

#2 using class reference
class studentdata():
    clg="narayana"
    def __init__(self,name,rollno,age,section):
        self.name=name
        self.rollno=rollno
        self.age=age
        self.section=section
    def progress(self):
        print(studentdata.clg,self.name,self.rollno,self.age,self.section)
a=studentdata("bhagya",33,25,"A")
a.progress()
studentdata("sasi",32,31,"A").progress()
print()

'''class studentdata():
    clg="narayana"
    def record(self,name,rollno,age,section):
        self.name=name
        self.rollno=rollno
        self.age=age
        self.section=section
    def progress(self):
        print(self.clg,self.name,self.rollno,self.age,self.section)
a=studentdata("bhagya",33,25,"A")
a.record
a.progress()   #type error'''

#3 using only normal method
class studentdata():
    clg="narayana"
    def record(self):
        name="bhagya"
        age=26
        rollno=33
        section="A"
        print(studentdata.clg,name,rollno,age,section)
a=studentdata()
a.record()
print()

#4 using only constructor
class studentdata():
    clg="chaitanya"
    def __init__(self,name,rollno,age,section):
        self.name=name
        self.rollno=rollno
        self.age=age
        self.section=section
        print(self.clg,self.name,self.rollno,self.age,self.section)
        
a=studentdata("bhagya",10,25,"A")
b=studentdata("sasi",11,31,"A")
c=studentdata("dharani",12,28,"A")
d=studentdata("ramesh",13,32,"A")
e=studentdata("riyanshi",14,5,"A")
print()

#5 using 2 normal methods
class studentdata():
    clg="narayana"
    def record(self):
        name="bhagya"
        age=26
        rollno=33
        section="A"
        print(studentdata.clg,name,rollno,age,section)
    def progress(self):
        name="sasi"
        age=31
        rollno=13
        section="A"
        print(studentdata.clg,name,rollno,age,section)
a=studentdata()
a.record()
a.progress()
