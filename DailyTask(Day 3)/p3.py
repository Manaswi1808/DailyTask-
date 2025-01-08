# Program to check if a number is positive, negative, or zero

# Take input from the user
number = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if number > 0:
    print(f"The number {number} is positive.")
elif number < 0:
    print(f"The number {number} is negative.")
else:
    print(f"The number {number} is zero.")
