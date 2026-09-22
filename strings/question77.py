# Write a program to find the first non-repeating character in a string

a= input('Enter the strings:')

for char in a:
  count=0

  for x in a:
    if char ==x:
      count+=1
  if count==1:
    print(char)   
    break 