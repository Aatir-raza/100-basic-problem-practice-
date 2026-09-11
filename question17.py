#wap to read a character and check whether it is alphabet , digit, or special symbol
a= (input('enter the charcter'))
if (a>='A' and a<='Z') or (a>='a'and a<='z'):
  print('ALphabet')
elif a>='0' and a<='9':
  print('digit') 
else:
  print('special symbols')

