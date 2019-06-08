class Addition():
     def add(self,a,b):
          return(a+b)
class Subraction():
     def sub(self,a,b):
          return(a-b)
class Multiplication():
     def mul(self,a,b):
          return(a*b)
class Division():
     def div(self,a,b):
          return(a/b)
class Result(Addition,Subraction,Multiplication,Division):
     def resultadd(self,a,b):
          print(r.add(a,b))
     def resultsub(self,a,b):
          print(r.sub(a,b))
     def resultmul(self,a,b):
          print(r.mul(a,b))
     def resultdiv(self,a,b):
          print(r.div(a,b))
      
          
r=Result()

print("1.Addition,2.Subraction,3.Multiplication,4.Division")
num1=int(input("enter a no:"))
num2=int(input("enter a no:"))

while(1):
     c=int(input("ënter the choice"))
     if(c==1):
          r.resultadd(num1,num2)
     elif(c==2):
          r.resultsub(num1,num2)
     elif(c==3):
          r.resultmul(num1,num2)
     elif(c==4):
          r.resultdiv(num1,num2)
     else:
           exit(0)
          
