word = input("Please type in a string:")
sub = input("Please type in a substring:")
index = word.find(sub)
index_sub = word.find(sub, index + len(sub))

if index_sub >= 0:
    print(f"The second occurrence of the substring is at index {index_sub}.")
else:
    print("The substring does not occur twice in the string.")
