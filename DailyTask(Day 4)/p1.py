# Function to calculate the division of two numbers
def div(numerator, denominator):
#numerator (float): The number to be divided.
#denominator (float): The number by which the numerator is divided.
    # Check if the denominator is zero to avoid division by zero error
    if denominator == 0:
        return "Error: Division by zero is not allowed."
    
    return numerator / denominator

# User input for the numerator and denominator
num1 = float(input("Enter the numerator: "))  # The numerator
num2 = float(input("Enter the denominator: "))  # The denominator

# Call the function and display the result
result = div(num1, num2)
print(f"The result of dividing {num1} by {num2} is: {result}")
