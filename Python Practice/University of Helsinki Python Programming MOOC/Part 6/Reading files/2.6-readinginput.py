def read_input(question:str, num1: int, num2: int):
    while True:
        try:
            inpnumber = int(input(f"{question}"))
            if inpnumber < min(num1, num2) or inpnumber > max(num1, num2):
                print(f"You must type in an integer between {min(num1,num2)} and {max(num1,num2)}")
            if min(num1, num2) <= inpnumber <= max(num1, num2):
                return inpnumber
        except ValueError:
            print(f"You must type in an integer between {min(num1,num2)} and {max(num1,num2)}")



if __name__ == "__main__":
    number = read_input("Please type in a number: ", 1, 5)
    print("You typed in:", number)
