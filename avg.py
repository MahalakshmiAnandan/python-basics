def student_name(a):
    return("enter student name:",a)
def reg_no(b):
    aa=b
    return('enter reg no:',b)
def marks(d,e):
    global aa
    return(aa,'eng:',d,'maths:',e)
def average():
    avg=0
    total=eng+maths
    avg=total/2
    return(avg)
aa=""
str="student details"
print(str)
name=input("enter the name:")
regno=int(input("enter reg no:"))
eng=int(input('enter marks:'))
maths=int(input('enter marks:'))

student_name(name)
reg_no(regno)
marks(eng,maths)
print(average())
    
