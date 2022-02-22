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