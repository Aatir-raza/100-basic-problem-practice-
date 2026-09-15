# Write a program to display all Armstrong numbers from 1 to n.

n=int(input('enter the number'))

for num in range(1,n+1):
  original=num
  temp=num
  sum=0

  while temp >0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
  if sum==original:
    print(num)
