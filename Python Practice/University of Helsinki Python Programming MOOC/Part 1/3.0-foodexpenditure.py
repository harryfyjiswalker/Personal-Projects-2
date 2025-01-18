freq = float(input("How many times a week do you eat at the student cafeteria?"))
price = float(input("The price of a typical student lunch?"))
spend = float(input("How much money do you spend on groceries in a week?"))

print(f"\nAverage food expenditure:\nDaily: {(freq*price+spend)/7} euros\nWeekly: {freq*price+spend} euros")
