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