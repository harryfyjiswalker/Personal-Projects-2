# Write your solution here
def first_word(sentence):
    i = 0
    while True:
        if sentence[i] != " ":
            i+=1
        else:
            break
    print(sentence[0:i])  

def second_word(sentence):
    i=0
    j=i+1
    while True:
        if sentence[i] != " ":
            i+=1
        else:
            i=i
            if sentence[j] !=" ":
                j+=1
            else:
                break
    print(sentence[0:i])

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    #print(first_word(sentence))
    print(second_word(sentence))
    #print(last_word(sentence))
