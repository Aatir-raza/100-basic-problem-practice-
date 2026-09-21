#Write a program to count the number of vowels and consonants in a string.

a=input('enter the string:')

vowels=0
consonants=0

for char in a:
  if char in "aeiouAEIOU":
    vowels=vowels+1
  else:
    consonants=consonants+1

print(vowels)
print(consonants)
