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


# %%
# Tuples
# Tuples are immutable
# Once assigned they cannot be changed

my_tuple = ("John", "Paul", 2)
print(my_tuple)
# %%
