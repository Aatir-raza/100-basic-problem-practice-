# Write a program to count the number of even and odd elements in an array.

a=int(input('enter the number:'))

even_count=0
odd_count=0

for i in range(a):
  element=int(input('enter the number:'))

  if element%2==0:
    even_count+=1
  else:
    odd_count+=1
print(even_count) 
print(odd_count)     