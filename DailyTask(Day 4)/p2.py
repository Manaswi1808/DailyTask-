#Declare a square() function with one parameter.Then call the function and pass one
# Function to calculate the square of a number
def square(x):
    # Return the square of the number
    return x ** 2

# User input for the number to be squared
num = float(input("Enter a number to square: "))

# Call the function and display the result
result = square(num)
print(f"The square of {num} is: {result}")
