# Divisible by 3
# ----------------
# As the user to input a number
# Check if any of the numbers is divisible by 3
# If the number is divisible by 3 print out you win
# and if not print out to try his luck next time
# The user has three chances.

# Method 1:
num = int(input("Enter a number: "))

if(num % 3 == 0):
    print("You win")
else:
    num = int(input("Enter a number: "))
    if(num % 3 == 0):
        print("You win")
    else:
        num = int(input("Enter a number: "))
        if(num % 3 == 0):
            print("You win")
        else:
            print("You lose")

