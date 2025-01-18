name = str(input("Person 1:\nName:"))
age = int(input("Age:"))
name2 = str(input("Person 2:\nName:"))
age2 = int(input("Age:"))
if age > age2:
    print(f"The elder is {name}")
elif age2 > age:
    print(f"The elder is {name2}")
else:
    print(f"{name} and {name2} are the same age")
