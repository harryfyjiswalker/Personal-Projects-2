def longest_series_of_neighbours(list1):
    lengthlist = []
    length = 1
    for i in range(len(list1)-1):
        list2 = float(list1[i]) + 1
        list3 = float(list1[i]) - 1
        if list1[i+1] == list2 or list1[i+1] == list3:
            length +=1
        else:
            length = 1
        lengthlist.append(length)
    return max(lengthlist)
        

if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))
