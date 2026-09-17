# Write a program to find the value of x raised to the power y without using inbuilt power.

x=int(input('enter the first number'))
y=int(input('enter the second number'))

result=1

for i in range(y):
  result=result*x
print(result)  