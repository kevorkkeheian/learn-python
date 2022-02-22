# Get the user:
# First name
# Last name
# Year of birth
# Calculate his/her age


from datetime import datetime, timedelta

birthday_text = input("enter your birthday (dd/mm/yyyy):")

current_date = datetime.now()
current_year = current_date.year

birthday = datetime.strptime(birthday_text, "%d/%m/%Y")

birth_year = birthday.year

print("your age is:" + str(current_year - birth_year))