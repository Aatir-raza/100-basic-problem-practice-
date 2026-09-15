# Write a program to check whether a number is a strong number (sum of factorials of its digits)

n=int(input('enter the number'))

original=n
sum=0

while n>0:
  digit=n%10
  fact =1
  for i in range(1,digit+1):
    fact*=i
  sum+=fact
  n//=10
if sum==original:    
  print('strong number')
else:
  print('not a strong number')

