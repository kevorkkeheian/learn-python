# Ask the user to input a number
# Check and print out if the number is a prime number
# prime number is only divisible by 1 and the number itself ( ex 7, 11, 17...)


# Method 1:
num = int(input("Please enter a number: "))
is_prime = True
count = 2

while count < num:
    if num % count == 0:
        is_prime = False
        break
    count += 1
if is_prime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

# Method 2:
num = int(input("Enter a number: "))
is_prime = True


for i in range (2, num):
    if num % i == 0:
        is_prime = False
        print(f"{num} is not a prime number because it is divisible by {i}")
        break

if is_prime:
    print(f"{num} is a prime number")