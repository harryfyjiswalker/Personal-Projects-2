wage = float(input("Hourly wage:"))
hours = float(input("Hours worked:"))
day = str(input("Day of the week:"))
if day == "Sunday":
    print(f"Daily wages: {wage*hours*2} euros")
else:
    print(f"Daily wages: {wage*hours} euros")
