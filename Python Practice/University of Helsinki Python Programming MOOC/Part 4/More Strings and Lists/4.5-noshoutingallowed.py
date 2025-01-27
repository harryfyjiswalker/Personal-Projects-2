def no_shouting(list1):
    list2=[]
    for i in range(len(list1)):
        if list1[i].isupper() != True:
            list2.append(list1[i])
    return list2

if __name__ == "__main__":
    list1 = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(list1)
    print(pruned_list)

