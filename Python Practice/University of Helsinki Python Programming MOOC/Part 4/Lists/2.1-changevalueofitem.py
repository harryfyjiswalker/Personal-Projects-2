list = [1, 2, 3, 4, 5]
index=0
while True:
    index = int(input("Index:"))
    if index != -1 and index <len(list):
        new_value = int(input("New value:"))
        list[index] = new_value
        print(list)
    else:
        break
