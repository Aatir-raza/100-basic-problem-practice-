# Write a program to check whether a number is a Harshad (Niven) number.
num=int(input('enter the number'))

original=num
digit_sum=0


while num>0:
  digit=num%10
  digit_sum+=digit
  num//=10

if original % digit_sum==0:
  print('harshad number')
else:
  print('not harshad number')  
  