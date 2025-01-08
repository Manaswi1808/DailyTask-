# Program to calculate net amount after discount based on toy type and order value

# Input: Toy type and order amount
product_code = int(input("Enter the product code (1 for Battery-Based, 2 for Key-Based, 3 for Electrical Charging-Based): "))
order_amount = float(input("Enter the order amount: "))

# Apply discount based on product code and order value
if product_code == 1:  # Battery-Based Toys
    if order_amount > 1000:
        discount = 0.10  # 10% discount
    else:
        discount = 0
elif product_code == 2:  # Key-Based Toys
    if order_amount > 100:
        discount = 0.05  # 5% discount
    else:
        discount = 0
elif product_code == 3:  # Electrical Charging-Based Toys
    if order_amount > 500:
        discount = 0.10  # 10% discount
    else:
        discount = 0
else:
    print("Invalid product code.")
    discount = 0

# Calculate the net amount after discount
net_amount = order_amount - (order_amount * discount)

# Display the result
print(f"Net amount to be paid: Rs. {net_amount:.2f}")
