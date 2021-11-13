


from os import pipe


def main():

    provinces = read_list("/home/andredosreis/Documentos/Estudos/BYU-Programming-with-fuctions/week-9/prepare/provinces.txt")

    print(provinces)
    
    #remove the first element from the list
    provinces.pop(0)

    #remove the last element from the list

    provinces.pop()
   
    for i in range(len(provinces)):
        if provinces[i] == 'AB':
            provinces[i] = 'Alberta'
    
    count  = provinces.count("Alberta")

    print()

    print(f'Alberta occurs {count} time is the modified list')


    


def read_list(filename):
    """Read the contents of a text file into a list
    and return the list that contains the lines of text.

    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    # Create an empty list named text_lines.
    text_lines = []

    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(filename, "rt") as text_file:

        # Read the contents of the text
        # file one line at a time.
        for line in text_file:

            # Remove white space, if there is any,
            # from the beginning and end of the line.
            clean_line = line.strip()

            # Append the clean line of text
            # onto the end of the list.
            text_lines.append(clean_line)

    # Return the list that contains the lines of text.
    return text_lines



if __name__ == "__main__":
    main()

    