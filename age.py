from datetime import date

age = input("Enter your birth year: ")

if (age.isdigit()):
    age = int(age)
else:
    print("Enter the year in integer.")

todays_date = date.today()
print(f"You are {todays_date.year - age} years old.")
