num = int(input("Please type in a number:"))
i = 1
if num % 2 == 0:
    while i < num:      
        print(i+1)
        print(i)
        i += 2
if num % 2 != 0:
    while i < (num-1):
        print(i+1)
        print(i)
        i+=2
    print(num)
