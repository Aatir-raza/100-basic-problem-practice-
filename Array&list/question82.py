# Write a program to find the largest and smallest element in an array

a=int(input('enter the array:'))

largest=0
smallest=0


for i in range(a):
  element=int(input('enter the number:'))

  if i==0:
    largest=element
    smallest=element

  if element>largest:
    largest=element

  if element<smallest:
    smallest=element
print(largest)
print(smallest)      