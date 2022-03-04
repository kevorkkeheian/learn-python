# Write a function to check whether a number is palindrome or not.

# Method 1
def is_palindrome1(number):
    # Convert the number to a string
    number_string = str(number)
    # Reverse the string
    number_string_reversed = number_string[::-1]
    # Compare the reversed string with the original string
    if number_string == number_string_reversed:
        return True
    else:
        return False

# Method 2:
def is_palindrome2(number):
    return str(number) == str(number)[::-1]



# Using method 1
num = 321231
if(is_palindrome1(num)):
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")

# Using method 2
num = 123211
if(is_palindrome2(num)):
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")