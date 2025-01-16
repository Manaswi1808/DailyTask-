# Lambda function to check if the number is positive, negative, or zero
check_number = lambda x: 'Positive' if x > 0 else 'Negative' if x < 0 else 'Zero'

# Test the lambda function with different numbers
num1 = float(input("Enter a number: "))
print(f"The number {num1} is {check_number(num1)}.")

num2 = float(input("Enter another number: "))
print(f"The number {num2} is {check_number(num2)}.")
