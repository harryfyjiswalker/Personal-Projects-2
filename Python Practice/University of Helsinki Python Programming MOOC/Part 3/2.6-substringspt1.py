string=input("Please type in a string:")
n = len(string)
for i in range(n+1):
    print(string[0:i])

#model answer:
string = input("Please type in a string: ")
 
length = 1
while length <= len(string):
    print(string[0:length])
    length += 1
 
