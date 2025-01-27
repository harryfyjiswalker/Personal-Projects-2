def longest_series_of_neighbours(list1):
    length = []
    for i in range(len(list1)-1):
        if abs(list1[i-1]-list1[i])==1:
            length[i].append(length[i-1] + 1)
        else:
            length=0
    return length

if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))
