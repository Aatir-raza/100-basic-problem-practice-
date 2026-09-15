# Write a program to check whether a number is a perfect number.
n= int(input('enter the number'))
sum=0

for i in range(1,n):
  if n%i==0:
   sum=sum + i
if sum==n:
  print('perfect number')
else:
  print('not a perfect number')     
  




