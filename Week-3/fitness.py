from datetime import datetime 

def main():
    
    gender = str(input('Please enter your gender (M or F): ')).strip().upper()[0]
    bir_date = str(input('Please enter your Birthdate (YYYY-MM-DD): '))
    lb = float(input('Enter your wight is US pounds:'))
    inches = float(input('Enter your height is US inches: '))

    years = compute_age(bir_date)
    print(f'Age (years): {years} ')

    
def compute_age(birth):
    """
    Computer and return a person's age in years.
    Parameter birth: a person's birthdate stored as a string in this format: YYYY-MM-DD
    Retorn: a person's age in years.
    """
    birthday = datetime.strptime(birth, "%y-%m-%d")
    today = datetime.now()

    #Computer the difference between today and the birthday in years.
    years = today.year - birthday.year
    
    #If necessery, subtract one from the difference.
    #if birthday.month > today.month:  # (birthday.month == today.month and birthday.day > today.day):
        #years -=1

    return years



main ()
