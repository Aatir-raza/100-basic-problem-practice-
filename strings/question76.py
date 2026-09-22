#  Write a program to check whether two strings are anagrams of each other.

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")


length1 = 0
for char in s1:
    length1 += 1


length2 = 0
for char in s2:
    length2 += 1

if length1 != length2:
    print("Not Anagram")

else:
    anagram = True

    for char in s1:

        count1 = 0
        count2 = 0

      
        for x in s1:
            if char == x:
                count1 += 1

        
        for x in s2:
            if char == x:
                count2 += 1

        if count1 != count2:
            anagram = False
            break

    if anagram:
        print("Anagram")
    else:
        print("Not Anagram")