#creating the files using file handling
a=open("file1.txt","w")
b=open("file2.txt","w")
c=open("file3.txt","w")
d=open("file4.txt","w")

#compress all the created files in one folder using zipfile    #doubt
from zipfile import *
e=ZipFile("files.zip","w")
e.write("file1.txt")
e.write("file2.txt")
e.write("file3.txt")
e.write("file4.txt")
e.close()
print("files created")

#to read zipfile
from zipfile import *
f=ZipFile("files.zip","r")
lists=f.namelist()
print(lists)

#to read zipfile using for loop
from zipfile import *
f=ZipFile("files.zip","r")
lists=f.namelist()
for i in lists:
    print(i)

#to read the content with in files which are in zip file #doubt
    
from zipfile import *
f=ZipFile("files.zip","r")
lists=f.namelist()
for i in lists:
    print(i)
    f1=open(i,"r")
    print(f1.read())
    print()

#to know current directory
import os
a=os.getcwd()
print("cwd",a)

#to create directories

import os
a=os.mkdir("sasi")


import os 
b=os.mkdir("aman/python")

import os
c=os.mkdir("file5.txt/file6.txt")


#to create multiple directories 

import os
a=os.makedirs("ramana/rama/dharani/bhagya")



#to remove dir

import os
b=os.rmdir("file5.txt/file6.txt")

#to remove directories

import os
b=os.removedirs("aman/python")