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

Model:
def find_words(search_term: str):
    results = []
 
    with open("words.txt") as file:
        # Tätä tarvitaan myöhemmin
        hakusana_ilman_tahtea = search_term.replace("*","")
 
        for word in file:
            word = word.replace("\n","")
            # Is there an asterisk?
            if "*" in search_term:
                # start or end?
                if search_term[0] == "*":
                    if word.endswith(hakusana_ilman_tahtea):
                        results.append(word)
                else:
                    if word.startswith(hakusana_ilman_tahtea):
                        results.append(word)
            # Is there a dot?
            elif "." in search_term:
                # same length?
                if len(search_term) == len(word):
                    found = True
                    for i in range(len(search_term)):
                        if search_term[i] != "." and search_term[i] != word[i]:
                            found = False
                            break
                    if found:
                        results.append(word)
            # No special characters, only whole word matches count
            else:
                if word == search_term:
                    results.append(word)
    return results
