phonebook = {}
number = []
while True:
    command = int(input("command(1 search, 2 add, 3 quit)"))
    if command ==3:
        break
    name = input("name:")
    if command == 1:
        if name in phonebook:
            for number in phonebook[name]:
                print(number)
        else:
            print("no number")
    elif command ==2:
        number = input("number:")
        if name in phonebook:
            phonebook[name].append(number)
        else:
            phonebook[name] = [number] 
        print("ok!")
print("quitting...")
