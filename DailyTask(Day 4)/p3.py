#Using max() and min() functions display the maximum and minimum of 5 random no
# User input for 5 random numbers
numbers = []
for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Find the maximum and minimum of the list
max_number = max(numbers)
min_number = min(numbers)

# Display the results
print(f"The maximum number is: {max_number}")
print(f"The minimum number is: {min_number}")
