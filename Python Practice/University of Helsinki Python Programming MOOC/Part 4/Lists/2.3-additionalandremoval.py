list = []
while True:
    print(f"The list is now {list}")
    adding = input("a(d)d, (r)remove or e(x)it:")
    if adding == "d":
        item = len(list) + 1
        list.append(item)
    elif adding == "r":
        list.pop(len(list)-1)
    elif adding == "x":
        break
print("Bye!")
