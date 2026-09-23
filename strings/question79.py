# Write a program to toggle the case of each character in a string.

a= input('Enter the strings:')

result=""

upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower='abcdefghijklmnopqrstuvwxyz'

for char in a:
  if char in upper:
    i=upper.index(char)
    result+=lower[i]
  if char in lower:
    i=lower.index(char)
    result+=upper[i] 

print(result)     

  
