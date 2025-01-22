sent = input("Please type in a sentence:")
index = sent.find(" ")
print(sent[0])
while index != -1: 
    print(sent[index+1])  
    index = sent.find(" ", index + 1)  
