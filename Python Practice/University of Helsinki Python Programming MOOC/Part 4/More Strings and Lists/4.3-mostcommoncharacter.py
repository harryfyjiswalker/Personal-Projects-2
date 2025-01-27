def most_common_character(string1):
    number = []
    for i in range(len(string1)):
        num = string1.count(string1[i])
        number.append(num)
        index = number.index(max(number))
    return string1[index]

if __name__ == "__main__":
    string1 = "abcdbde"
    print(most_common_character(string1))
