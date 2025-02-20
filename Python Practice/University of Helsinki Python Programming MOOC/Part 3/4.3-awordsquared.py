def squared(string1:str, num:int):
    list1 = []
    while len(list1) <= num**2:
        for i in range(len(string1)):
            list1.append(string1[i])
    for j in range(0, num**2, num):
        printable = list1[j:j+num]
        print(''.join(map(str, printable)))


if __name__ == "__main__":
    squared("ab", 3)
