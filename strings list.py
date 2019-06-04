a="%^&haasj73737"
list1=[]
list2=[]
list3=[]
for i in range(0,len(a)):
 if(a[i].isalpha()==True):
  list1.append(a[i])
 elif(a[i].isdigit()==True):
  list2.append(a[i])
 else:
  list3.append(a[i])
print(list1)
print(list2)
print(list3)
