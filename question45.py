# WAP to display all prime number 1 to n.
n=int(input('enter the number'))


for num in range(2,n+1):
  prime= True

  for i in range (2,num):
    if num %i ==0:
      prime=False
      break
  if prime:
    print(num)   