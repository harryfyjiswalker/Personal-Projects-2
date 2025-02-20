def first_word(sentence):
    i = 0
    while True:
        if sentence[i] != " ":
            i+=1
        else:
            break
    return sentence[0:i]

def second_word(sentence):
    list1=[]
    indexes = []
    for i in range(len(sentence)):
        list1.append(sentence[i])
    for i in range(len(list1)):
        if list1[i] == ' ':
            indexes.append(i)
    if len(indexes) == 1:
        secondword = list1[indexes[0]+1:len(sentence)]
    else:
        secondword = list1[indexes[0]+1:indexes[1]]
    return ''.join(map(str, secondword))

def last_word(sentence):
    list2=[]
    indexes1 = []
    for i in range(len(sentence)):
        list2.append(sentence[i])
    for i in range(len(list2)):
        if list2[i] == ' ':
            indexes1.append(i)
    lastword = list2[indexes1[-1]+1:len(sentence)]
    return ''.join(map(str, lastword))


# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
