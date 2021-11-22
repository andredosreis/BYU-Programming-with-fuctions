import csv
from datetime import datetime

products = {}
def main():

    
 try:
    
    file_products = input("Enter the name of text file (products.csv): ")  
    products = read_products(file_products)
    print("\n")
    

    for key, value in products.items():
        print(key, value)

    item = 0
    subtotal = 0
    tax = 0
    total = 0
    
    print("\n")
    
    file_request = input("Enter the name of text file(request.csv): ")  
    with open(file_request, "rt") as csvFile:
        csvReader = csv.reader(csvFile)
        next(csvReader)
        print("\n")
        print("INKOM EMPORIUM\n")
        
        for row in csvReader:
            product = products[row[0]]
            name = product[0]
            price = float(product[1])
            quantity = int(row[1])
        
            print(f'{name}: {quantity} @ {price}')

            item += quantity
            subtotal += price * quantity 
            tax = subtotal * 0.06
            total = tax + subtotal
            
        print(f'number of item: {item}')
        print(f'subtotal: {subtotal:.2f}')
        print(f'Sales Tax: {tax:.2f}' )
        print(f'Total: {total:.2f}')
        current_date_and_time = datetime.now()
        
        print(f"Thank you for shopping at the INKOM EMPORIUM .\n{current_date_and_time:%c}")
        print("\n")
        
        #keyError test
        key = input(" Enter with the product number: ")
        product = products[key]
        print(f'This the product key {product[0]}')
        
         
    
 except (FileNotFoundError, PermissionError) as error:
        print(error)
        print("Please, run the program again and enter the" \
                " name of an existing file.")
        
 except KeyError as error:
        print("Please, This is a Keyerror, run this program again and enter with a product key that is in file product.csv.")
        
    
def read_products(fileName):


    with open(fileName, 'rt') as csvFile:
        
        csvReader = csv.reader(csvFile)
        
        next(csvReader)
        
        for row in csvReader:
            products[row[0]] = row[1:]
        
        return products   
        
if __name__ == "_main_":
    main()