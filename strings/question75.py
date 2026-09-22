#  Write a program to remove all spaces from a string.

a= input('Enter the strings:')
result= ""

for char in a:
  if char!=" " :
    result+=char
  
print(result)