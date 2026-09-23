# Write a program to replace all occurrences of a character with another character in a string

a=input('enter the string:' )


old_char=input('enter the strings:')
new_char=input('enter the strings')
result=''

for char in a:
  if char==old_char:
    result+=new_char
  else:
    result+=char  
print(result)    