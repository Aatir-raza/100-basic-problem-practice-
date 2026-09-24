# Write a program to remove duplicate elements from an array.

arr = [1, 2, 2, 3, 1, 4]

result = []

for element in arr:
    if element not in result:
        result.append(element)

print(result)



    
  
