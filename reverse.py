n=int(input())
sum=0
while n>0:
 print(n,end="")
 r=n%10
 print(r,end="")
 sum=sum*10+r
 print(sum)
 n=n//10
 print("reversed no:",sum)
