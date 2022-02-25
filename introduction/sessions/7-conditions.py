# %% [markdown]
# # 7 - Handling Conditions

# %% [markdown]
# #### 1 - If Statement

# %%
# Tax Example


# Let the user input the price by converting it to a float
price = float(input("Enter the price: "))

# Start the condition
if price >= 1000:
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
if price >= 10000:
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


if price >= 1000:

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
