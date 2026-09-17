#Write a program to display the first n terms of the Fibonacci series

n=int(input('enter the  number'))

a=0
b=1

for i  in range(n):
  print(a,end="")

  c=a+b
  a=b
  b=c
