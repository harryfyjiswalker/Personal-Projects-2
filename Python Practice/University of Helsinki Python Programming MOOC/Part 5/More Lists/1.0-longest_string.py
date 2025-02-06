def longest(strings:list):
    length = []
    for string in strings:
        length.append(len(string))
    return strings[length.index(max(length))]

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))
    
