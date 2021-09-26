import math
from datetime import datetime

print('-=' *52)
print('')

print('                          Welcome our market place of the BYUI ')
print('')
print('You can chose width,ratio and diameter, we have three options of tires, 165/65/14, 205/55/16, 175/70/14  ')
print('')
print('-=' *52)

wt = float(input('Enter the width of tire in  mm '))
rt = float(input('Enter the aspect ratio of the tire '))
diam = float(input('Enter the diameter of the wheel in inches '))

#volume = math.pi * wt**2 * rt * (wt * rt + 2540 * diam) / 10000000000

date_now = datetime.now()
date_of_week = date_now.weekday()

if wt != 165 and wt != 205 and wt != 175:
    print('Please enter wiht values correct! ')
    wt = float(input('Enter the width of tire in  mm '))
    rt = float(input('Enter the aspect ratio of the tire '))
    diam = float(input('Enter the diameter of the wheel in inches '))

if wt == 165 and rt == 65 and diam == 14:
            print(f'The price of Tire is $62.80')
            
elif wt == 205 and rt == 55 and diam == 16:
            print(f'The price of Tire is $56.42')
            
elif wt == 175  and rt == 70 and diam == 14:
            print(f'The price of Tire is $36.19')

buy = str(input('Do you Want buy this Tire? [Y/N]')).strip().upper()[0]
        




if buy == 'Y':
    phone = str(input('Please put your tephone number '))
    with open('volumes.txt',  'at') as volume_file:
        print(f'{phone} {date_now:%y-%m-%d}', file=volume_file)
elif buy == 'N':
    print('thanks')

      
    
     
print('Check back often')


#with open('dimensions.txt',  'wt') as dimens_file:
    #print(model, file = dimens_file)
    #print(f'{wt}, {rt}, {diam}, {date_now:%d-%m-%y}', file=dimens_file)
 #   print(f'{volume:.2f} liters, {date_now: %d-%m-%y}', file=dimens_file)


#print(f'The approximate volume is {volume:.2f} liters')


