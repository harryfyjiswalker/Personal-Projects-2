with open("dictionary.txt", "a+") as new_file:
    new_file.seek(0) #move pointer to beginning of file
    lines = new_file.readlines()
    dictionary = {line.split(" - ")[1].strip(): line.split(" - ")[0] for line in lines if " - " in line} #read all lines from file and create dic

    while True:
        print("1 - Add word, 2 - Search, 3 - Quit")
        inp = int(input("Function: "))
        
        if inp == 1:
            inp1 = input("The word in Finnish: ")
            inp2 = input("The word in English: ")
            dictionary[inp2] = inp1
            new_file.seek(0) #move pointer to beginning to overwrite content
            new_file.truncate()  # Clear the file content
            for k, v in dictionary.items():
                new_file.write(f"{v} - {k}\n")
            print("Dictionary entry added")
        
        elif inp == 2:
            inp3 = input("Search term: ").lower()
            found = False
            for k, v in dictionary.items():
                if inp3 in k.lower() or inp3 in v.lower():
                    print(f"{v} - {k}")
                    found = True
            if not found:
                print("Word not found in the dictionary.")
        
        elif inp == 3:
            break
    
    print("Bye!")
