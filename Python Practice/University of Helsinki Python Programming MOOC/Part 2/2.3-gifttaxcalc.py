gift = float(input("Value of gift:"))
if gift >= 1000000:
    print(f"Amount of tax: {142100+(gift-1000000)*0.17}")
if 200000 <= gift < 1000000:
    print(f"Amount of tax: {22100+(gift-200000)*0.15}")
if 55000 <= gift < 200000:
    print(f"Amount of tax: {4700+(gift-55000)*0.12}")
if 25000 <= gift < 55000:
    print(f"Amount of tax: {1700+(gift-25000)*0.10}")
if 5000 <= gift < 25000:
    print(f"Amount of tax: {100+(gift-5000)*0.08}")
if gift < 5000:
    print("No tax!")
