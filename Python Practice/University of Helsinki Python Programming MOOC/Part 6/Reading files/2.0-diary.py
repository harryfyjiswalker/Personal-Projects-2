with open("diary.txt", "r+") as new_file:
    #print(f)
    while True:
        print("1 - add an entry, 2 - read entries, 0 - quit")
        func = int(input("Function:"))
        if func == 1:
            entry = input("Diary entry: ")
            new_file.write(f"{entry}\n")
            print("Diary saved")
        elif func == 2:
            new_file.seek(0) #move pointer to beginning before reading
            print("Entries:")
            print(new_file.read())
        elif func == 0:
            break
    print("Bye now!")
