# wap to find largest digit in a number n .
n=(input('enter the number'))
largest=0
for digit in n:
  if int(digit)>largest:
   largest=int(digit)
print(largest)  
