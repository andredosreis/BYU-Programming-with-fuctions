import math

wt = float(input('Enter the width of tire in  mm '))
rt = float(input('Enter the aspect ratio of the tire '))
diam = float(input('Enter the diameter of the wheel in inches '))

volume = math.pi * wt**2 * rt * (wt * rt + 2540 * diam) / 10000000000

print (f' The approximate volume is {volume:.2f} litres ')

