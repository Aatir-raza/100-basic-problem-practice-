# WAP  to find the sum of the first and last digit of a number n .

n=int(input('enter the number'))

last=n%10

while n>=10:
  n=n//10

first=n
print(first+last)  