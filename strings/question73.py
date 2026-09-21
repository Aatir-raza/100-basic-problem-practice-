#  Write a program to convert a string to uppercase and lowercase without inbuilt case functions

s = input("Enter a string: ")

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"

result_upper = ""
result_lower = ""

for char in s:
    if char in lower:
        i = lower.index(char)
        result_upper += upper[i]
        result_lower += char

    elif char in upper:
        i = upper.index(char)
        result_lower += lower[i]
        result_upper += char

    else:
        result_upper += char
        result_lower += char

print("Uppercase:", result_upper)
print("Lowercase:", result_lower)
  