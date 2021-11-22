import csv
from datetime import datetime

products = {}
def main():
    
    products = read_products("/home/andredosreis/Documentos/Estudos/BYU-Programming-with-fuctions/week-10/prove/products.csv")
    print("\n")
    print("PRODUCTS\n")

    for key, value in products.items():
        print(key, value)
    #print(products)
    
    item = 0
    subtotal = 0
        
   
    with open('/home/andredosreis/Documentos/Estudos/BYU-Programming-with-fuctions/week-10/prove/request.csv', 'rt') as csvFile:
        csvReader = csv.reader(csvFile)
        next(csvReader)
        print('')
        print("REQUEST ITEMS\n")
        
        for row in csvReader:
            product = products[row[0]]
            name = product[0]
            price = float(product[1])
            quantity = int(row[1])

                        
            print(f'{name}: {quantity} @ {price}')

        

            item += quantity
            subtotal += price * quantity 
            taxe = subtotal * 0.06
            total = taxe + subtotal
            
        print()
        print(f'Number of Itens: {item}')
        print(f'Subtotal: {subtotal:.2f}')
        print(f'Sale Taxe: {taxe:.2f}' )
        print(f'Total: {total:.2f}')
    print()  
    current_date_and_time = datetime.now()
    print(f"Thank you for shopping at the Inkom Emporium.\n{current_date_and_time:%c}")
print()        



try:
        with open("/home/andredosreis/Documentos/Estudos/BYU-Programming-with-fuctions/week-10/prove/products.csv", "rt") as products_file:
            for line in products_file:
                print(line)

except FileNotFoundError as not_found_err:

        print(not_found_err)




try:
    with open("/home/andredosreis/Documentos/Estudos/BYU-Programming-with-fuctions/week-10/prove/products.csv", "rt") as contacts_file:
        for line in contacts_file:
            print(line)

except PermissionError as perm_err:
    print(perm_err)

try:
       
        products = {}
       
        name = products["50-420-1021"]

        print(name)

except KeyError as key_err:
        print(type(key_err).__name__, key_err)








def read_products(fileName):

    

    with open(fileName, 'rt') as csvFile:
        
        csvReader = csv.reader(csvFile)
        
        next(csvReader)
        

        for row in csvReader:
            products[row[0]] = row[1:]
        
        return products
            
          
if __name__ == "__main__":
    main()