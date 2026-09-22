#  Write a program to count the frequency of each character in a string.

a=input('enter the strings:')


freq={}

for char in a:
  if char in freq:
    freq[char]+=1
  else:
    freq[char]=1
print(freq)       