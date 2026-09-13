#wap to replace all zeros in a number n with the digit 5

n=(input('enter the number'))

new=""

for digit in  n:
  if digit=='0':
    digit='5'

  new=new + digit
print(new)  


 

