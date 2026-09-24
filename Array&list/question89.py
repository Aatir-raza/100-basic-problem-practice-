# Write a program to sort an array in ascending order (bubble sort).

arr = [5, 3, 8, 1, 2]

n = 0

for element in arr:
    n += 1

for i in range(n):
    for j in range(n - 1 - i):

        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)

