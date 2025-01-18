num1 = int(input("Number 1:"))
num2 = int(input("Number 2:"))
op = str(input("Operation:"))
if op == "multiply":
    print(f"{num1} * {num2} = {num1*num2}")
if op == "add":
    print(f"{num1} + {num2} = {num1+num2}")
if op == "subtract":
    print(f"{num1} - {num2} = {num1-num2}")
