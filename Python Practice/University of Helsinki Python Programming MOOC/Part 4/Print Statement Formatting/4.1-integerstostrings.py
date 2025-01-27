def formatted(list1):
    new_list = []
    for i in range(len(list1)):
        new_list.append(f"{list1[i]:.2f}")
    return new_list

if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)
