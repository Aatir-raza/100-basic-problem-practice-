#  Write a program to check whether a number is an automorphic number.

n= int(input('enter the number'))

original=n
square=n**2

digit=0
temp=n

while temp >0:
  digit+=1
  temp//=10

last_digit=square%(10**digit) 

if last_digit==original:
  print('automorphic number')
else:
  print('not a automorphic number')  

