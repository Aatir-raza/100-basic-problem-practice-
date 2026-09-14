# Write a program to display the first n prime numbers.
n=int(input('enter the number'))
count=0
num=2

while count <n:
  prime=True

  for i in range (2,num):
      if num %i ==0:
        prime=False
        break
      
  if prime:
    print(num)
    count=count+1

  num=num+1

