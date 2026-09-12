# wap to find the product of all natural numbers from 1 to n (factorial of n)

n=(int(input('enter the  number')))
product=1
for i in range(1,n+1):
  product= product*i
print(product)  