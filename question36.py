# wap to find the  product of all digit of  a number n.

n=input('enter the number ')
prod=1

for digit in n :
  prod=prod*int(digit)
print(prod)
