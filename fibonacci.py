n=int(input())
s1=0
s2=0
for i in range(0,n):
 if i<=1:
  sum=i
 else:
  sum=s1+s2
  s1,s2=s2,sum
print(sum)
