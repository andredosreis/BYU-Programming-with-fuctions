import csv
from datetime import datetime

all_product = {}
PRODUCT_INXEX = 0
NAME_INDEX = 1
PRICE_INDEX = 2
QUANTITY_INDEX = 1
PRODUCT_REQUEST_INDEX = 0
def main():

   

    read_product_store = read_product("/home/andredosreis/Documentos/Estudos/BYU-Programming-with-fuctions/week-9/Prove/products.csv",PRODUCT_INXEX, NAME_INDEX,PRICE_INDEX)
    
    try: 

        file_product =  input("Enter the name of text file (products.csv): ")
        all_product = read_product(file_product)
        print('\n')

        for key, value in all_product.items():
            print(key,value)

        item = 0
        subtotal = 0
        
        print('\n')

        file_request = input("Enter the name of text file(request.csv): ")
        with open('/home/andredosreis/Documentos/Estudos/BYU-Programming-with-fuctions/week-9/Prove/request.csv', 'rt') as csvfile:

            csvreader = csv.reader(csvfile)
            next(csvreader)
            print('REQUEST ITENS\n')

            
            for row in csvreader:
                product = all_product[row[PRODUCT_INXEX]]
                name = product[0]
                price = float(product[1])
                quantity = int(row[1])

                print(f'{name}: {quantity} @ {price}')

                item += quantity
                subtotal += price *quantity
                taxe = subtotal * 0.06
                total = taxe + subtotal

            print()

            print(f'Number of Itens: {item}')
            print(f'Subtotal: {subtotal:.2f} ')
            print(f'Sale Taxe:{taxe:.2f} ')
            print(f'Total: {total:.2f}')
        print()

        current_date_and_time = datetime.now()
        print(f'Thank you for shopping at the Inkom Emporium.\n{current_date_and_time:%c}')

        key = input(" Enter with the product number: ")
            product = all_product[key]
            print(f'This the product key {product[0]}')

        except (FileNotFoundError, PermissionError) as error:
            print(error)
            print("Please, run the program again and enter the" \
                    " name of an existing file.")
            
        except KeyError as error:
            print("Please, This is a Keyerror, run this program again and enter with a product key that is in file product.csv.")
        
  
def read_product(filename, key_product, value_name, value_price):
    
    with open(filename, "rt") as infile:

        reader = csv.reader(infile)

        next(reader)

        for row in reader:

            product = row[key_product]
            name = row[value_name]
            price = row[value_price]

            all_product[product] = [name, price]
    return all_product


if __name__ == "__main__":
    main()

