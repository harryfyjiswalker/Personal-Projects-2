import math
string = input("Please type in a string:")
length = (28 - float(len(string)))/2
print(30*"*")
print("*"+" "*math.ceil(length)+string+" "* math.floor(length) + "*")
print(30*"*")

#model answer:
word = input("Word: ")
 
print("*" * 30)
spaces_at_start = (28 - len(word)) // 2
spaces_at_end = spaces_at_start
 
# If the word length is odd, one is added to the spaces at the end of the word
# to get all 30 characters filled
if len(word) % 2 != 0:
    spaces_at_end += 1
 
print("*" + spaces_at_start * " " + word + spaces_at_end * " " + "*")
print("*" * 30)
 
