word = input("Please type in a word:")
char = input("Please type in a character:")
index = word.find(char)
if len(word)-index>=3:
    if char in word:
        print(word[index:index+3])
    else:
        print("")
else:
    print("")
