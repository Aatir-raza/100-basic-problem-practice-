# Write a program to find the sum and average of all elements in an array

a= int(input('enter the array:'))

sum=0
average=0

for i in range (a):
  element=int(input('enter the element:'))
  sum=element+sum
average=sum/a
print(sum) 
print(average) 
