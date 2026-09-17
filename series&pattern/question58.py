#  Write a program to find the sum of the first n terms of the Fibonacci series

n=int(input('enter the  number'))

a=0
b=1
sum=0

for i  in range(n):
  sum=sum+a

  c=a+b
  a=b
  b=c
print(sum)
