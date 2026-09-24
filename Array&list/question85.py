# Write a program to reverse the elements of an array
n=[]
a=int(input('enter the array:'))


for i in range(a):
  number=int(input('enter the number:'))
  n.append(number)
print(n)  

for i in range(a-1,-1,-1):
  print(n[i])

