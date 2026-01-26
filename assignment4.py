
# Program to convert inches into different units

# Input from user
inches = float(input("Enter measurement in inches: "))

# Conversions
foot = inches / 12
yard = inches / 36
centimeter = inches * 2.54
meter = inches / 39.37

# Display results
print("Feet:", foot)
print("Yards:", yard)
print("Centimeters:", centimeter)
print("Meters:", meter)
