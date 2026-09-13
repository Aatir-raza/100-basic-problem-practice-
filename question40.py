# wap to count the number of even digit and odd digit in a number n
n=(input('enter the number'))

even=0
odd=0

for digit in  n:
  if int(digit)%2==0:
    even=even+1
  else:
    odd=odd+1
     
print('Even digits',even)
print('Odd digits',odd)