# wap to find smallest digit in a number n .
n=(input('enter the number'))
smallest= int(n[0])
for digit in n:
  if int(digit)<smallest:
   smallest=int(digit)
print(smallest)  
