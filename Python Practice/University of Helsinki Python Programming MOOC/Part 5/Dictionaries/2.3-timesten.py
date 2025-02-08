def times_ten(start_index: int, end_index: int):
    dict = {}
    for i in range(start_index, end_index+1):
        dict[i] = 10*i
    return dict


if __name__ == "__main__":
    d = times_ten(1, 3)
    print(d)
