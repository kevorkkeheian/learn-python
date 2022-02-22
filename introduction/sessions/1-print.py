# %% [markdown]
# # 1 - Print

# %% [markdown]
# `print()` is build in function in python that takes any type of object as it's parameter
# 
# The [print](https://docs.python.org/3/library/functions.html#print) function let's you send an output to the terminal 
# 
# 
# Python [built-in functions](https://docs.python.org/3/library/functions.html)

# %%
print("Hello, World!")

# %% [markdown]
# You can enclose strings in **double** quotes (" ") or **single** quotes (' ')

# %%
print('Hello, World!')

# %% [markdown]
# In case you have to use a signle quote in a string (for example: I'm a string) you can use the escape sequence (\) or use double quotes for the string

# %%
print("I'm a string")
print('I\'m a string')

# %% [markdown]
# You can combine strings with + or , <br />
# The difference is that + concatenates strings, while , joins strings

# %%
# Concatinate strings with sign +
print("Hello, " + "World!")
print("Hello,", "World!", "!")

# %% [markdown]
# How to print a new line in python?

# %%
print("Hello, World!")

# print a blank line
print()
print("This is a new line")

# %%
# print a line with \n
# \n is a special character sequence that tells Python to start a new line
print("This is the first line \nThis is the second line")

# %%
# print a line with a tab
print("This is a regular line")
print("\tThis is a new line with a tab")

# %% [markdown]
# Another usefull built-in function in python is `input()` <br />
# It allows you to prompt the user to input a value <br />
# But you need to declare a variable to hold the user's value in it

# %%
# Here name is variable that will hold the user's input
name = input("Please eneter your name: ")

print("Your name is:", name)