def length_of_longest(list1):
    longest = 0
    for i in range(len(list1)):
        if len(list1[i])>longest:
            longest = len(list1[i])
    return longest

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = length_of_longest(my_list)
    print(result)
