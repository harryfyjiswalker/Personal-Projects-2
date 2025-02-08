def histogram(word: str):
    repeats = {}
    for char in word:
        if char not in repeats:  
            repeats[char] = "*" * int(word.count(char))
    for key, value in repeats.items():
        print(key, value)

if __name__ == "__main__":
    histogram("abba")
