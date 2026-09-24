# Write a program to find the second largest element in an array

n = int(input("Enter number of elements: "))

largest = 0
second_largest = 0

for i in range(n):
    element = int(input("Enter element: "))

    if element > largest:
        second_largest = largest
        largest = element

    elif element > second_largest:
        second_largest = element

print(second_largest)

