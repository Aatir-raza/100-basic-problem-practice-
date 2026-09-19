# Write a program to print a pyramid pattern of stars of height n.


n= int(input('enter the height'))

for i in range (1,n+1):
  spaces=n-i
  stars=2*i-1

  print(" "*spaces + "*"* stars)
