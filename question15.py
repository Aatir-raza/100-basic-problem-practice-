#wap to read a year and check whether it is a leap year or not
a=int(input('enter the year'))
if a%400==0:
  print('leap year')
elif a% 100 ==0:
  print('not leap year')

elif a%4==0:
  print('leap year')
else:
  print('not leap year')

