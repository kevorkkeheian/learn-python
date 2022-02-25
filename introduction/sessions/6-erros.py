

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
