# wap to check whether a number n is a palindrome 

n=int(input('enter  the number'))

original=n
reverse=0

while n>0:
  digit=n%10
  reverse=reverse*10 + digit
  n=n//10
  
if reverse==original:
  print('palindrome')
else:
  print('not palindrome')  