#Write a program to find the sum of all even-indexed and odd-indexed elements separately

arr = [10, 20, 30, 40, 50]

even_sum = 0
odd_sum = 0

n = 0

for element in arr:
    n += 1

for i in range(n):
    if i % 2 == 0:
        even_sum = even_sum + arr[i]
    else:
        odd_sum = odd_sum + arr[i]

print( even_sum)
print( odd_sum)
  