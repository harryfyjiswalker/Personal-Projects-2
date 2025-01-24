list = []
while True:
    num = int(input("New item:"))
    if num != 0:
        list.append(num)
        print(f"The list now: {list}")
        print(f"The list in order: {sorted(list)}")
    if num == 0:
        break
print("Bye!")
