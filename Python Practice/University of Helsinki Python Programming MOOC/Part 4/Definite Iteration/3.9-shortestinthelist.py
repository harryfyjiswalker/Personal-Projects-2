def shortest(list1):
    shortest = list1[0]
    for i in range(1,len(list1)):
        if len(list1[i]) < len(shortest):
            shortest = list1[i]
    return shortest

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = shortest(my_list)
    print(result)
