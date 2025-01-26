def palindromes(word1):
    list1 = list(word1)
    if list1==list1[::-1]:
        return True
    else:
        return False

while True:
    word1=input("Please type in a palindrome:")
    if palindromes(word1) == False:
        print("that wasn't a palindrome")
    elif palindromes(word1) == True:
        print(f"{word1} is a palindrome!")
        break
    

#if __name__ == "__main__":
    #word1="neveroddoreven"
    #print(palindromes(word1))

