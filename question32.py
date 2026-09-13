# wap to count how many numbers from 1 to n are divisible by 3 or 5

n=int(input('enter the numbers '))

for i in range (1,n+1):
  if i%3==0 or i%5==0:

   print(i)    
