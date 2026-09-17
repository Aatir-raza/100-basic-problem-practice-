# Write a program to find the GCD (HCF) of two numbers

a=int(input('enter the first number'))
b=int(input('enter the second number'))

hcf=0

for i in range(1,min(a,b)+1):
  if a%i==0 and b%i==0:
    hcf=i
print(hcf)    