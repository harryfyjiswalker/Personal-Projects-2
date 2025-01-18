string=input("Please type in a string:")
n = 0
while n<=len(string):
    print(string[len(string)-n:len(string)])
    n += 1
