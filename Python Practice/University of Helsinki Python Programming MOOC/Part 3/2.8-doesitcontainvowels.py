string = input("Please type in a string:")
letters = ["a", "e", "o"]
m=len(letters)
for i in range(m):
    if letters[i] in string:
        print(letters[i]+" found")
    else:
        print(letters[i]+" not found")
