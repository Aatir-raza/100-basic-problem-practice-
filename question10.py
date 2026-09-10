seconds=int(input('enter the second'))
hours=seconds//3600
remaining=seconds%3600
minutes=remaining//60
seconds=remaining%60
print(hours,minutes,seconds)
