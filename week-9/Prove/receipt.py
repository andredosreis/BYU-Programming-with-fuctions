import csv

all_product = {}
def main():

    PRODUCT_INXEX = 0
    NAME_INDEX = 1
    PRICE_INDEX = 2
    QUANTITY_INDEX = 1
    PRODUCT_REQUEST_INDEX = 0

    read_product_store = read_product("/home/andredosreis/Documentos/Estudos/BYU-Programming-with-fuctions/week-9/Prove/products.csv",PRODUCT_INXEX, NAME_INDEX,PRICE_INDEX)
   # print(read_product_store) 

    with open("/home/andredosreis/Documentos/Estudos/BYU-Programming-with-fuctions/week-9/Prove/request.csv",  'rt') as request_file:

        request = csv.reader(request_file)

        print(request)
        next(request)

        

        for row in request:

            product_name = row[0]
            quantity = row[QUANTITY_INDEX]
            price = row[PRICE_INDEX]

            all_product[product_name] = [quantity, price]

            print(all_product)
            




         


  #          print(product, quantity)



  
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

