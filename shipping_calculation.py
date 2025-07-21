#Shipping cost calculator

## Input package weight and shipping rate.
weight = float(input("Enter package weight in kilograms: "))
shipping_rate = float(input("Enter shipping rate per kilogram: "))

# Calculate the shipping cost.
shipping_cost = weight * shipping_rate

# Display the cost.
print(f"The shipping cost is ${shipping_cost}.")
