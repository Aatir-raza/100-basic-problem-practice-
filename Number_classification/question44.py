# WAP to read  a number and check whether it is prime or not 

n=int(input('enter the number'))

prime=True

if n<2:
  prime=False
else:
  for i in range (2,n):
   if n%i==0:
    prime=False
    break
if prime:
  print('prime number')
else:
  print('not prime')  