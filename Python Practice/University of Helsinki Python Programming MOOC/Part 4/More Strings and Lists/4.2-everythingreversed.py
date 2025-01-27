def everything_reversed(list1):
    new_list =[]
    for i in range(len(list1)-1, -1, -1):
        string1 = f"{list1[i]}"
        rev = string1[::-1]
        new_list.append(rev)
    return new_list

if __name__ == "__main__":
    list1 = ["Hi", "there", "example", "one more"]
    print(everything_reversed(list1))
