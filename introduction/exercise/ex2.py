# Ask user to give a number representing a year.

# Note:A leap year is divisible by 4, unless it is an end-of-century year (divisible by 100) which must be divisible by 400 as well.

# Examples:2000 → Leap year (divisible by 4, divisible by 100, divisible by 400)
# 1997 → Not a leap year (NOT divisible by 4)
# 1000 → Not a leap year (divisible by 4, divisible by 100, NOT divisible by 400)
# 2024 → Leap year (divisible by 4, NOT divisible by 100)


year = int(input("Enter a year: "))

# Method 1:

print("--- Method 1 ---")
# Check if year is divisible by 100
if year % 100 == 0:
    # Check if divisible by 400
    if year % 400 == 0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
else:
    # Check if divisible by 4
    if year % 4 == 0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")



# Method 2:
print("--- Method 2 ---")

if  year % 4 == 0 and year % 100 != 0:
    print(f"{year} is a leap year")

elif year % 100 == 0 and year % 400 == 0:
    print(f"{year} is a leap year")

else:
    print(f"{year} is not a leap year")
