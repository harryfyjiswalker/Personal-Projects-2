words = []
while True:
    word = input("Please type in a word: ")

    if word == "end":
        break

    elif len(words) > 0 and word == words[-1]:
        break

    words.append(word)

sentence = " ".join(words)

print(sentence)

#Model solution
story = ""
previous = ""
while True:
    word = input("Please type in a word: ")
    if word == "end" or word == previous:
        break
    story += word + " "
    previous = word
 
print(story)
