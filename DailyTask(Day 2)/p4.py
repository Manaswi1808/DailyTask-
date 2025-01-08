# Take input from the user
principal_amount = float(input("Enter the principal amount (Rs.): "))
annual_interest_rate = float(input("Enter the rate of interest (% per year): "))
time_period_years = float(input("Enter the time period (in years): "))

# Calculate Simple Interest
simple_interest = (principal_amount * annual_interest_rate * time_period_years) / 100

# Display the result
print(f"The Simple Interest on Rs. {principal_amount} for {time_period_years} years at {annual_interest_rate}% per year is Rs. {simple_interest}.")
