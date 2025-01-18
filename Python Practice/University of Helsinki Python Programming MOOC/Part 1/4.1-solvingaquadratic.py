from math import sqrt

a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))

disc = b**2 - 4*a*c

x_1 = (-b + sqrt(disc))/(2*a)
x_2 = (-b - sqrt(disc))/(2*a)
print(f"The roots are {x_1} and {x_2}.")
