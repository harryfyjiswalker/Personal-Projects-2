list = []
while True:
    word = input("Word:")
    if word not in list:
        list.append(word)
    else:
        break
print(f"You typed in {len(list)} different words")
