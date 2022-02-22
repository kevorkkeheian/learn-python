# %% [markdown]
# # 2- Comments

# %% [markdown]
# In any programming language, you can use comments to write notes to yourself or other developers. <br />
# And comments, of course, are not executed in the program

# %%
print("Hello World")
# print("Hello World")

# %% [markdown]
# You can use comments to: 
# - explain what the code does and to make it more readable.
# - debug your code

# %%
# ask the user for his name
name = input("Please enter your name: ")

# output a greeting message
print("Hello", name)

# %%
name = input("Please enter your name: ")

# This code is used to check if the user's name
print("The user has entered:", name)


print("Hello", name)

# %% [markdown]
# # 3 - String Variables

# %% [markdown]
# ### Strings in variables

# %%
# You can store a string in a variable
first_name = "John"

# And use that same variable to output a greeting
print("Hello", first_name)

# %% [markdown]
# ### Combining strings

# %% [markdown]
# You can combine strings with + or , <br />
# The difference is that `+` concatenates strings, while `,` joins strings

# %%
first_name = "John"
last_name = "Doe"

print(first_name + last_name)


# And if you want to add a space between the two names
print(first_name + " " + last_name)

#or
print(first_name, last_name)

# you can't use , to concatinate strings when storing them in a variable
# they will be stored as a variable rather than a string
full_name = first_name, last_name
print(full_name)

# %% [markdown]
# ### Formatting strings

# %% [markdown]
# Most of the data types in programming languages have built-in methods
# In python the methods used with string are called **string functions**

# %%
phrase = "My dog is named Lucky"

# To make the whole phrase capitalized, you can use upper()
print(phrase.upper())

# To make the whole phrase lowercase, you can use lower()
print(phrase.lower())

# To make the first letter of each word capitalized, you can use title()
print(phrase.title())

# To make only first letter capital, you can use capitalize()
print(phrase.capitalize())

# %%
# Ask the user for their first and last name
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')

print ('Hello ' + first_name.capitalize() + ' ' + last_name.capitalize())

# %% [markdown]
# # 4 - Numeric Variables

# %% [markdown]
# As we mentioned earlier we have many data types in python
# numeric data types are:
# - Integers: `int`
# - Floats: `float`
# - Complex numbers: `complex`

# %%
# integers:
num = 5
print(num)
print(type(num))

# floats:
num = 5.0
print(num)
print(type(num))

#complex:
num = 5 + 3j
print(num)
print(type(num))

# %% [markdown]
# The same way as string variables, numeric variables can be printed

# %%
pi = 3.14159
print(pi)

# %% [markdown]
# In python you can use mathematical operations with numeric variables

# %% [markdown]
# Python is a dynamicly typed language <br />
# Which means that type checking is done on runtime <br />
# The other type is staticly typed language, which is when type checking is done at compile time <br />

# %% [markdown]
# When variables are assigned string values, python knows that it is a string <br />
# It is the same when the variable is assigned a numeric value <br />

# %%
# assign two variables
first_num = 9
second_num = 4

#addition
print(first_num + second_num)

#subtraction
print(first_num - second_num)

#multiplication
print(first_num * second_num)

#division
print(first_num / second_num)

#modulus
print(first_num % second_num)

#exponent
print(first_num ** second_num)


# %% [markdown]
# You can also treat a numeric variable as a string

# %%
first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")

# because the numbers are entered as strings
# When you print first_number + second_number, you will get a concatinated string
print(first_number + second_number)


# %% [markdown]
# But if you want to print the sum of both numbers you can use conversion methods

# %%
first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")

# 1 - you can use the int() function
#print(int(first_number) + int(second_number))

# 2 - you can use the float() function
print(float(first_number) + float(second_number))


# Check if first_number is integer
if isinstance(int(first_number), int):
    print("first_number is an integer")

# %%
months = 12
print(months)

# This list will result in an error
# Because you cannot concatinate an integer with a string
print(months + " months in a year")

# You need to convert the integer to a string using str()
print(str(months) + " months in a year")    

# %% [markdown]
# Because python is dynamically types <br />
# You can change the type of a variable on runtime

# %%
name = "111"
print(name)
print(type(name))

name = 1
print(name)
print(type(name))

# %% [markdown]
# # 5 - Dates

# %% [markdown]
# To use the date variable in python you need to import package datetime from datetime library
# This is done by using the import statement

# %%
from datetime import datetime

# you can get the current date in python with:
today = datetime.now()

# Like numeric values you need to convert date variables to strings to be able to concatinate with another string
print("Today is: " + str(today))

# %% [markdown]
# Now if you want to input a date you need to convert the user's input to a date format

# %%
from datetime import datetime


birthday = input("Enter your birthday (dd/mm/yyyy): ")

# To convert a string to a date variable you can use the datetime.strptime() function
# The first argument is the string to convert
# The second argument is the format of the string
# The third argument is the date variable to store the converted string
# The datetime.strptime() function returns a datetime object
birthday_date = datetime.strptime(birthday, "%d/%m/%Y")
print(birthday_date)

# You can use the strftime() function to convert the date variable to a string
# The first argument is the date variable to convert
# The second argument is the format of the string
# The strftime() function returns a string
# A is the weekday, %B is the month, %d is the day, %Y is the year
birthday_date_name = birthday_date.strftime("%A %d %B %Y")
print("Your birthday is: " + birthday_date_name)


# %% [markdown]
# Like any other data type in python, datetime has his own functions

# %%
from datetime import datetime, timedelta

# To get the current date
today = datetime.now()

# You can add or remove days, weeks, hours, minutes, seconds, microseconds
yesterday = today - timedelta(days=1)
print(yesterday)
tomorrow = today + timedelta(days=1)
print(tomorrow)

next_week = today + timedelta(weeks=1)
print(next_week)

next_month = today + timedelta(weeks=4)
print(next_month)
print(next_month.month)
print(next_month.strftime("%B"))

# %% [markdown]
# You can get parts of a datetime object

# %%
from datetime import datetime

today = datetime.now()
print("Day:", today.day)
print("Month:", today.month)
print("Year:", today.year)

print("Hour:", today.hour)
print("Minute:", today.minute)
print("Second:", today.second)

# %% [markdown]
# # 6 - Error Handling

# %% [markdown]
# There are many ways to handle an error in python

# %% [markdown]
# #### 1 - Syntax Errors

# %%
# 1 - Syntax errors

x = 42
y = 50

if(x == y)
    print("Success!")

# %% [markdown]
# #### 2 - Runtime Errors

# %%
# 2 - Runtime errors

x = 10
y = 0

print(x / y)

# %% [markdown]
# #### 3 - Try and Catch/Except

# %%
# Try and catch
x = 10
y = 0

try:
    print(x / y)

except ZeroDivisionError as e:
    print("Something went wrong")
except:
    print("Something really went wrong, but it's not division by zero")
finally:
    print("This always runs on success or failure")


# %% [markdown]
# #### 4 - Logic Errors

# %%
# 3 - Logic Error
x, y = 3, 4

if(x < y):
    print(str(x), "is greater than", str(y))

# %% [markdown]
# # 7 - Handling Conditions

# %% [markdown]
# #### 1 - If Statement

# %%
# Tax Example


# Let the user input the price by converting it to a float
price = float(input("Enter the price: "))

# Start the condition
if price >= 10.00:
    # If the price is greater than or equal to 1.00
    # Then the tax is 0.15
    tax = 0.15
    print(f"The price is: {price + (price * tax)}")


# %% [markdown]
# #### 2 - If-Else Statement

# %%
# Let the user input the price by converting it to a float
price = float(input("Enter the price: "))

# Start the condition
if price >= 10.00:
    # If the price is greater than or equal to 1.00
    # Then the tax is 0.15
    tax = 0.15
    print(f"The price is: {price + (price * tax)}")

else:
    # If the price is less than 1.00
    # Then the tax is 0.10
    tax = 0.10
    print(f"The price is: {price + (price * tax)}")

# %% [markdown]
# #### 3 - Different Indentation

# %%
# Let the user input the price by converting it to a float
price = float(input("Enter the price: "))


if price >= 10.00:

    tax = 0.15
    print(f"The price is: {price + (price * tax)}")

else:
    tax = 0.10

# Here the line is not indented wrong, but the code is not correct
print(f"The price is: {price + (price * tax)}")

# %% [markdown]
# #### 4 - Comparing strings

# %%
country = "Lebanon"

# Case sensitive comparison
if country == "Lebanon":
    print("You are in Lebanon")
else:
    print("You are not in Lebanon")



# Case insensitive comparison
if country.lower() == "lebanon":
    print("You are in Lebanon")
else:
    print("You are not in Lebanon")

# %% [markdown]
# #### 5 - Multiple Conditions

# %%
# Multiple if statements

# You can use multiple if statements
# But when the code runs, will not stop at the first condition that results true

province = input("Enter your province: ")

# Because python is dynamically typed, you need to declare a variable by assigning it to 0
tax = 0

if province.lower() == "maten":
    tax = 0.05
if province.lower() == "beirut":
    tax = 0.10
if province.lower() == "bekaa":    
    tax = 0.15

print(f"The tax is: {tax}")


# %%
# Elif statements

# If you use elif the code will stop at the first condition that results true
province = input("Enter your province: ")

# Because python is dynamically typed, you need to declare a variable by assigning it to 0
tax = 0

if province.lower() == "maten":
    tax = 0.05
elif province.lower() == "beirut":
    tax = 0.10
elif province.lower() == "bekaa":    
    tax = 0.15
else:
    tax = 0.20

print(f"The tax is: {tax}")

# %%
# Nested if statements

country = input("Enter your country: ")

if country.lower() == "lebanon":
    province = input("Enter your province: ")
    if province.lower() == "maten":
        print("You are in Maten")
    elif province.lower() == "beirut":
        print("You are in Beirut")
    elif province.lower() == "bekaa":
        print("You are in Bekaa")
    else:
        print("We are not familiar with that province")
else:
    print("You are not in Lebanon")

# %% [markdown]
# #### 6 - Complex Conditions

# %%
# Use in statement

province = input("Enter your province: ")

if province in ("maten", "beirut", "bekaa"):
    print("You are in Lebanon")
else:
    print("You are not in Lebanon")

# %%
# Use or statement

if province == "maten" or province == "beirut" or province == "bekaa":
    print("You are in Lebanon")
else:
    print("You are not in Lebanon")

# %%
# Use and statement

print("Answer the following questions")
quiz_one = input("5 * 5 = ")
quiz_two = input("5 * 2 = ")
quiz_othree = input("3 * 4 = ")

if(quiz_one == "25" and quiz_two == "10" and quiz_othree == "12"):
    print("You win")
else:
    print("You lose")

# %%
# You can use boolean variables to save the state of the condition

print("Answer the following questions")
quiz_one = input("5 * 5 = ")
quiz_two = input("5 * 2 = ")
quiz_othree = input("3 * 4 = ")

if(quiz_one == "25" and quiz_two == "10" and quiz_othree == "12"):
    user_has_one = True
else:
    user_has_one = False

if(user_has_one):
    print("You win")
else:
    print("You lose")

# %% [markdown]
# # 8 - Collections

# %% [markdown]
# #### 1 - Lists

# %%
# Declare and assign the names
names = ["John", "Paul", "George"]

# Print the list of names
print(names)

# Add a new name
names.append("Jane")

# Declare and ass the scores
numbers = [100, 80, 90]

# Print the scores
print(numbers)

# Add a new score
numbers.append(70)


# Create a list of numbers and names
my_list = [100, 90, 80, "John", "Jane"]

# Print my_list
print(my_list)

# Add a new name
my_list.append("Paul")

# Add a new number
my_list.append(70)

# Print my_list
print(my_list)


# sorting a list will not work if the list contains more than 1 type of data
#my_list.sort()
numbers = numbers.sort()
print(numbers)
names.sort()
print(names)

# %% [markdown]
# #### 2 - Arrays
# 
# Arrays can only contain one type of data

# %%
# Declare and create an array of numbers
numbers = [2, 6, 5, 4, 3]


# Print numbers
print(numbers)

# Add a new number
numbers.append(1)

# Print numbers
print(numbers)


# Declare and assign the names
names = ["John", "Paul", "George"]

# Insert a new value in the list
names.insert(1, "Pauline") # Insert Pauline at index 1 and move the others to the right
print(names)


# Get the length of the list
print(len(names))



# %% [markdown]
# #### 3 - Common operations

# %%
# Declare and create an array of numbers
numbers = [2, 6, 5, 4, 3]

# Sort the numbers and save it in the same variable

print(sorted(numbers))
numbers.sort(reverse=False)
print(numbers)

# print number at index 1
print(numbers[1])

# Print a range of numbers
print(numbers[1:3])
print(numbers[:3])
print(numbers[1:])


# %% [markdown]
# #### 4 - Dictionaries

# %%
# Create a person dictionary
person = { "first_name": "John", "last_name": "Doe", "age": 30, "city": "Beirut", "country": "Lebabon" }

# Print the first name of the person
print(person["first_name"])

# %% [markdown]
# # 9 - Loops

# %% [markdown]
# #### 1 - For Loop

# %%
names = ["John", "Paul", "George"]



# Here name is a newly declared variable that changes its value for every element in the names list
for name in names:
    print(name)

# %% [markdown]
# #### 2 - Numbers

# %%
for i in range(0, 5):
    print(i)

# %% [markdown]
# #### 3 - While Loop

# %%
names = ["John", "Paul", "George", "Jane"]
index = 0


while index < len(names):
    print(names[index])
    index += 1

# %% [markdown]
# # 10 - Functions

# %%
# In this example we will check how much time the function took to complete

from datetime import datetime

def print_time():
    print(datetime.now())
    print()


print_time()

for i in range(0, 1000):
    print(i)

print_time()

# %%
# This example will get the initials of the user

def get_initials(name):
    return name[0]


first_name = input("Please enter your first name: ")
first_name_initials = get_initials(first_name)

last_name = input("Please enter your last name: ")
last_name_initials = get_initials(last_name)


# Print the initials
print(f"Your initials are: {first_name_initials}{last_name_initials}")


# Or you can print the initials without assigning them to a variable
print(f"Your initials are: {get_initials(first_name)}{get_initials(last_name)}")

# %%
# Functions with multiple parameters

def get_initials(name, force_uppercase):
    if force_uppercase:
        return name[0].upper()
    else:
        return name[0]

first_name = input("Please enter your first name: ")
first_name_initials = get_initials(first_name, True)

last_name = input("Please enter your last name: ")
last_name_initials = get_initials(last_name, False)

print(f"Your initials are: {first_name_initials}{last_name_initials}")


