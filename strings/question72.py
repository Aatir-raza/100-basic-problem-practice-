# Write a program to check whether a string is a palindrome.
 
a=input('enter the strings:')
reverse=""

for char in a:
  reverse=char+reverse

if a==reverse:
    print('string is palindrome') 
else:
    print('not palindrome')  