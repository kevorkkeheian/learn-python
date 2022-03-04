# %% [markdown]
# # 10 - Functions

# %%
# In this example we will check how much time the function took to complete

from cgitb import reset
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



# %%
# 03032020

# This is a function that prints the sum of the 2 parameters
def add(a, b):
    print(a + b)

add(3, 4)


# %%
# Functions with default parameters
def print_message(is_uppercase = False, message = "Hello World"):
    if is_uppercase:
        print(message.upper())
    else:
        print(message)

# print the message
print_message()

# print message with uppercase
print_message(True)

# print message with custom message
print_message(message = "Printin a custom message")

# %%

# How to reverse a string??
name = "kevork"
# [start:end:step] 
# - start is the index where to start 
# - end is the index where to end, 
#  - step is the step size
test1 = name[1:3:2]
test2 = name[2::-1]
test3 = name[1::3]

name_reversed = name[::-1]

print(name_reversed)


# %%

# Lambda functions

def fun_compute():
    return lambda x: x * x

#result = fun_compute()

print(fun_compute(2))

# %%
