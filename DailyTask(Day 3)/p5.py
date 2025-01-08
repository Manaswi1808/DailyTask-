# Program to calculate the transport fare based on distance

# Input: Distance traveled
distance = float(input("Enter the distance traveled in kilometers: "))

# Calculate fare based on distance
if distance <= 50:
    fare = distance * 8  # 8 Rs./Km for 1-50 km
elif distance <= 100:
    fare = distance * 10  # 10 Rs./Km for 51-100 km
else:
    fare = distance * 12  # 12 Rs./Km for > 100 km

# Display the fare
print(f"The transport fare for {distance} km is Rs. {fare:.2f}")
