from math import sqrt

# Taking input from the user
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

# Calculate discriminant
disc = b**2 - 4*a*c

# Check if discriminant is negative
if disc < 0:
    print("The equation has complex roots.")
else:
    # Calculate roots if discriminant is non-negative
    x_1 = (-b + sqrt(disc)) / (2 * a)
    x_2 = (-b - sqrt(disc)) / (2 * a)
    print(f"The roots are {x_1} and {x_2}")
