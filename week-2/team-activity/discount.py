from datetime import datetime

sub_total = float(input('Please enter the subtotal:'))
tax = float(input('Sales tax amount: '))

date_now = datetime.now()
date_of_week = date_now.weekday()
total = sub_total * tax / 100 


if date_of_week == 1:
    desc = sub_total * 0.1
    total_desc = sub_total - desc + total


    print(' your days is tuesday')

print(f'discount amount: {desc:.2f}')
print(f'Sales tax amount: {tax:}')
print(f'Tatal: { total_desc:.2f}')
