# Write your solution here
def same_chars(string, int1, int2):
    if int1 < len(string) and int2 <len(string):
        if string[int1] == string[int2]:
            return True
        else:
            return False
    else:
        return False


# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
