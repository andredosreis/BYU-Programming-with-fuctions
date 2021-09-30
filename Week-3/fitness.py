from datetime import datetime

def main():
    gender = input('What is your gender ')
    bir = input(' What is your Birthdate (YYYY-MM-DD)')
    hei = float(input('What is your height (Inches)'))
    wei = float(input('What is your weigtht (LB) '))

    years = compute_age(bir)
    kg = kg_from_lb(wei)
    cm = cm_from_in(hei)
    Bmi = body_mass_index()
    pass
 