# Ask user to give a temperature in Celsius degrees, then
# convert it to Fahrenheit degrees.
# Temperature below -271.15°C (absolute zero) does not exist.
# Sample input and output:
# C 0 → F 32
# C 100 → F 212
# C -300 → "Invalid. Temperature below absolute zero"


temperature = float(input("Enter a temperature in Celsius degrees: "))

if temperature < -271.15:
    print("Invalid. Temperature below absolute zero")
else:
    fahrenheit = (temperature * (9/5)) + 32
    print(f"F {fahrenheit}")