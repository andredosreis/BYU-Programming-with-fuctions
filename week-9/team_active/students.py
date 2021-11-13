
import csv

def main():
    #keys
    I_NUMEBER = 0
    #values
    STUDENT_NAMES = 1

    Id_num = read_dict('/home/andredosreis/Documentos/Estudos/BYU-Programming-with-fuctions/week-9/team_active/students.csv', I_NUMEBER, STUDENT_NAMES)
    
    print(f'{Id_num} ')


def read_dict(filename, key_column_index, value_colum):
    
    dictionary = {}

    with open(filename, 'rt') as csv_file:
        
        reader = csv.reader(csv_file)

        #the first line of the CSV file contains column
        #headings and not information 
        next(reader)

        for row in reader:

            Id_number = row[key_column_index]
            studant_name = row[value_colum]
            

            dictionary[Id_number] = [studant_name]

    return dictionary


if __name__ == "__main__":
    main()

    



