import csv
with open("studentmarksrecord.csv","w",newline='') as f:
    w=csv.writer(f)
    w.writerow(["student_name","student_rollno","Maths_marks","English marks","Hindi_marks","Science_marks","Social_marks","Total_marks","Average_marks","Percentage","Result"])
    n=int(input("enter number of employee to entry details: "))
    for i in range(1,n+1):
        print(i," STUDENTS MARKS DEATILS ")
        stuname=input("enter name : ")
        sturollno=int(input("enter rollno :"))
        maths=int(input("enter maths marks :"))
        english=int(input("enter english marks : "))
        hindi=int(input("enter hindi marks :"))
        science=int(input("enter science marks :"))
        social=int(input("enter social marks:"))
        x=(maths+english+hindi+science+social)
        total=x
        y=x/5
        avg=y
        z=x/500*100
        per=z
        result="pass" if per>=35 else "fail"
    
        w.writerow([stuname,sturollno,maths,english,hindi,science,social,total,avg,per,result])
    print("totsl emp data written to csv file ")