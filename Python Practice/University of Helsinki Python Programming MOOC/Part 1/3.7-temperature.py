temp = int(input("Please type in a temperature (F):"))
temp_C = (temp - 32) * (5/9)
print(f"{temp} degrees Fahrenheit equals {temp_C} degrees Celsius")
if temp_C < 0:
    print("Brr! It's cold in here!")
