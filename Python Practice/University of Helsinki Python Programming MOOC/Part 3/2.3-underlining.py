while True:
    string = input("Please type in a string:")
    if len(string) != 0: #or if string == "":
        print(string)
        print("-"*int(len(string)))
    else:
        break
