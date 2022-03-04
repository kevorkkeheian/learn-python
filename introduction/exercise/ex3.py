# Negative or Positive

# Ask the user to input a number between -1000 and 1000
# Check and print out if the number is negative or positive 

num = int(input("Enter a number: "))

if num < 1000 and num > -1000:
    if num < 0:
        print(f"{num} is a negative number")
    elif num > 0:
        print(f"{num} is a positive number")
    else:
        print(f"{num} is zero") 
else:
    print("Number is not between -1000 and 1000")


