import csv
 #keys
I_NUMEBER_INDEX = 0
    #values
STUDENT_NAMES_INDEX = 1

def main():

    with open('/home/andredosreis/Documentos/Estudos/BYU-Programming-with-fuctions/week-9/team_active/students.csv', 'rt') as students_file:

        reader  = csv.reader(students_file)
        # The first line of the CSV file contains column headings
        # and not information about a dental office, so this
        # statement skips the first line of the CSV file.
        next(reader)

         # Read each row in the CSV file one at a time.
        # The reader object returns each row as a list

        for row in reader:

            sudets = row[STUDENT_NAMES_INDEX]
            num_I = int(row[I_NUMEBER_INDEX])

    print(f'numeber numeber ID is {num_I} and the is {sudets}')





        
