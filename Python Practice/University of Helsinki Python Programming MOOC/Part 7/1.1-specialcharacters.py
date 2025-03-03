from string import ascii_letters
from string import punctuation

def separate_characters(my_string:str):
    parts1 = []
    parts2 = []
    parts3 = []
    for i in range(len(my_string)):
        if my_string[i] in ascii_letters:
            parts1.append(my_string[i])
        elif my_string[i] in punctuation:
            parts2.append(my_string[i])
        elif my_string[i] not in ascii_letters or punctuation:
            parts3.append(my_string[i])
    tuple1 = ("".join(map(str,parts1)), "".join(map(str,parts2)), "".join(map(str,parts3)))
    return tuple1

    

if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])
