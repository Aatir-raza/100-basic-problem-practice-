# Write a program to find the sum of the series 1 + 2 + 3 + ... + n

n=int(input('enter the number'))


sum=0

for i in range(1,n+1):
  sum=sum+i
  
print(sum)  