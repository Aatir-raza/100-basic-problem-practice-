# Write a program to check whether a number is an Armstrong number.

n= int(input('enter the number'))

original=n
sum=0

while n>0:
  digit=n%10
  sum=sum+ digit **3
  n=n//10

if sum==original:
  print('armstrong number')
else:
  print('not armstrong number')    