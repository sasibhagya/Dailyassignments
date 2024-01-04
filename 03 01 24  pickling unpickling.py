l=[1,2,3,4,5,8,2,5,4,6]
target=9
for i in range(len(l) - 1):
    for j in range(i + 1, len(l)):
        if l[i] + l[j] == target:
            print("sum of two values:" ,l[i],"+",l[j],"=",target)


#pickling and unpickling

import pickle

class Employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
    def display(self):
        print(self.eno,"/t",self.ename,"/t",self.esal)

with open("emp.data","wb") as f:
    b=Employee(244,"raju",20000)  
    e=Employee(233,"aman",10000)
    c=Employee(225,"bhagya",25000)
    pickle.dump(b,f) 
    pickle.dump(e,f)
    pickle.dump(c,f)
    
    print("pickle of emp object is done ")

#unpickle

with open("emp.data","rb") as g:
    obj=pickle.load(g)
    obj2=pickle.load(g)
    obj3=pickle.load(g)
    obj.display()
    obj2.display()
    obj3.display()



class Studentdata():
    def __init__(self,stuname,sturollno,stuage,stucourse,stuaddress):
        self.stuname=stuname
        self.sturollno=sturollno
        self.stuage=stuage
        self.stucourse=stucourse
        self.stuaddress=stuaddress
    print("Each student data:")
    def progress(self):
        print(self.stuname,"---",self.sturollno,"---",self.stuage,"---",self.stucourse,"---",self.stuaddress)

obj=Studentdata("bhagya",101,26,"python","Hyderabad") 
obj.progress()      
obj2=Studentdata("sasi",102,31,"devops","Hyderabad")
obj2.progress()


import pickle
class Studentdata():
    def __init__(self,stuname,sturollno,stuage,stucourse,stuaddress):
        self.stuname=stuname
        self.sturollno=sturollno
        self.stuage=stuage
        self.stucourse=stucourse
        self.stuaddress=stuaddress
    print("Each student data:")
    def progress(self):
        print(self.stuname,"---",self.sturollno,"---",self.stuage,"---",self.stucourse,"---",self.stuaddress)
#pickling
with open("student.data","wb") as f:
    obj=Studentdata("bhagya",101,26,"python","Hyderabad")       
    obj2=Studentdata("sasi",102,31,"devops","Hyderabad")   
    pickle.dump(obj,f)
    pickle.dump(obj2,f)
#unpickling
with open("student.data","rb") as g:
    obj=pickle.load(g)
    obj.progress()
    obj2=pickle.load(g)
    obj2.progress()