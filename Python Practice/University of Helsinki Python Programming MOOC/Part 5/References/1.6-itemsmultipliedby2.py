def double_items(numbers: list):
    new_list = []
    for i in range(len(numbers)):
        new_list.append(2*numbers[i])
    return new_list

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)
