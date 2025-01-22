word = input("Please type in a word:")
char = input("Please type in a character:")
index = word.find(char)  # find first occurrence of char

while index != -1 and len(word) - index >= 3:  # only enter loop if char found + only if three or less
    print(word[index:index + 3])  # Print 3 characters starting from the index
    index = word.find(char, index + 1)  # Find the next occurrence, starting from the next index. If not found, does not enter while loop
