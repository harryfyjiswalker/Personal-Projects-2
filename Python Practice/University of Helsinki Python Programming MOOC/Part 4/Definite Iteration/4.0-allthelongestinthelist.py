def length_of_longest(list1):
    longest = 0
    for i in range(len(list1)):
        if len(list1[i])>longest:
            longest = len(list1[i])
    return longest

def all_the_longest(list1):
    new_list = []
    for i in range(len(list1)):
        if len(list1[i]) == length_of_longest(list1):
            new_list.append(list1[i])
    return new_list

if __name__ == "__main__":
    list1 = ["first", "second", "fourth", "eleventh"]
    result = all_the_longest(list1)
    print(result) # ['eleventh']
