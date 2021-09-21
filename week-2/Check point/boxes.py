import math

num = int(input('Enter the number of items: '))
box = int(input('Enter the number of items per box: '))

div = num / box
resu = math.ceil(div)

print(f'For {num} items, packing {box} in each box, you will need {resu} boxes.')
