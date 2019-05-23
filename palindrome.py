n=int(input())
sum=0
temp=n
while n>0:
 r=n%10
 sum=sum*10+r
 n=n//10
if sum==temp:
 print("palindrome")
else:
 print("not palindrome")
