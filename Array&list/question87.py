# Write a program to count the frequency of each element in an array

n=int(input('Enter the array:'))
arr=[]


for i in range(n):
  number=int(input('Enter the number:'))
  arr.append(number)

for i in range(n):
  count=0

  for j in range(n):
    if arr[i]==arr[j]:
      count+=1

  print(arr[i],count)      
  
