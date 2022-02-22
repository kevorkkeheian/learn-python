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