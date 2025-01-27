def no_vowels(string1):
    string2 = ""
    for i in range(len(string1)):
        if string1[i] not in "aeiou":
            string2 += string1[i]
    return string2


if __name__ == "__main__":
    string1 = "this is an example"
    print(no_vowels(string1))
