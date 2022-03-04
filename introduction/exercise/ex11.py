# Write a Python function to check whether a number is perfect or not.


# Method 1:
def check_perfect1(number):
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    if sum == number:
        return True
    else:
        return False

# Method 2:
def check_perfect2(number):
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    return sum == number


num = int(input("Enter a number: "))

# Using method 1
if check_perfect1(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")

# Using method 2
if check_perfect2(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")