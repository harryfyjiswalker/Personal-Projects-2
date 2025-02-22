import itertools

def find_words(word:str):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    with open("words.txt") as new_file:
        result = []
        possible_words = []
        indexes = []
        if word.startswith("*"):
            for line in new_file:
                line = line.replace("\n", "")
                if line.endswith(word[1:]):
                    result.append(line)
        if word.endswith("*"):
            for line in new_file:
                line = line.replace("\n", "")
                if line.startswith(word[0:len(word)-1]):
                    result.append(line)
        if "." in word:
            a = list(word)
            #print(a)
            for i in range(len(a)):
                if a[i] == ".":
                    indexes.append(i)
            possible_combinations = itertools.product(alphabet, repeat=len(indexes))
            for combination in possible_combinations:
                new_word = list(word)
                for index, char in zip(indexes, combination):
                    new_word[index] = char
                possible_words.append("".join(new_word))
            #print(possible_words)
            for line in new_file:
                line = line.replace("\n", "")
                for j in range(len(possible_words)):
                    if possible_words[j] == line:
                        result.append(line)
        else:
            for line in new_file:
                line = line.replace("\n", "")
                if word in line:
                    result.append(line)
        return result

if __name__ == "__main__":
    find_words("*vokes")
