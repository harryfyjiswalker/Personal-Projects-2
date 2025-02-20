text = input("Write text: ")
nonsplitlist = text.split(" ")
text_lower = text.lower()
splitting = text_lower.split(" ")

with open("wordlist.txt") as new_file:
    wordlist = set(line.strip() for line in new_file)
    for i in range(len(splitting)):
        if splitting[i] in wordlist:
            print(nonsplitlist[i], end=" ")
        if splitting[i] not in wordlist:
            print(f"*{nonsplitlist[i]}*", end=" ")
