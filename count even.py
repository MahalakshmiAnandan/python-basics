a=int(input())
b=int(input())
count=0
for i in range(a,b):
 if(i%7==0 and i%2==0):
  count=count+1
  print(count)
  
