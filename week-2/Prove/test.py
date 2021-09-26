from datetime import datetime

current_date_and_time = datetime.now()

print(f'{current_date_and_time:%d-%m-%y}')

model = 'GMC Acadia'
length = 193
width = 75
height = 67

with open('dimensions.txt',  'at') as dimens_file:
    print(model, file = dimens_file)
    print(f'{length}, {width}, {height}, {current_date_and_time:%d-%m-%y}', file=dimens_file)
