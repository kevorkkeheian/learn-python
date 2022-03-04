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
