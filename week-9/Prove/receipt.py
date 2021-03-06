import csv
from datetime import datetime

all_product = {}
def main():
    try:
        with open("/home/andredosreis/Documentos/Estudos/BYU-Programming-with-fuctions/week-10/prove/products.csv", "rt") as products_file:
            for line in products_file:
                print(line)

    
        PRODUCT_INXEX = 0
        NAME_INDEX = 1
        PRICE_INDEX = 2
        QUANTITY_INDEX = 1
        PRODUCT_REQUEST_INDEX = 0

        read_product_store = read_product("/home/andredosreis/Documentos/Estudos/BYU-Programming-with-fuctions/week-9/Prove/products.csv",PRODUCT_INXEX, NAME_INDEX,PRICE_INDEX)
        
        for key, value in read_product_store.items():
            print(key,value)

        item = 0
        subtotal = 0
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

    except (FileNotFoundError, PermissionError) as not_found_err:

        print(not_found_err)

    except KeyError as error:
        print('please, this a keyerror, run this program again and enter a product')
  
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

