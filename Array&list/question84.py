#Write a program to search for an element in an array (linear search).

a = int(input("Enter number of elements: "))
search = int(input("Enter element to search: "))

for i in range(a):
    element = int(input("Enter element: "))

    if element == search:
        print("Element found")
        break
        
else:
    print("Element not found")

    
