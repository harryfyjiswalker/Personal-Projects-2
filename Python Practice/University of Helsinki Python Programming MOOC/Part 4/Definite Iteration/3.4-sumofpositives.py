def sum_of_positives (my_list):
    my_list_pos = []
    for i in range(len(my_list)):
        if my_list[i] > 0:
            my_list_pos.append(my_list[i])
        result = sum(my_list_pos)
    return result

if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    print("The result is", sum_of_positives(my_list))
