#Write a program to find the LCM of two numbers.

a=int(input('enter the first number'))
b=int(input('enter the second number'))

lcm=max(a,b)


while True:
  if lcm%a==0 and lcm%b==0:
    break
  lcm+=1
print(lcm)


