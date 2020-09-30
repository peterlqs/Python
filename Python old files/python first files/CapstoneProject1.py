import math
p=input('For PI, How many decimal places would you like?')
try:
    b='{:.'+ p + 'f}'
    print(b)
    print('PI = ' + b.format(math.pi))
except ValueError:
    print("Please type in a number!")

