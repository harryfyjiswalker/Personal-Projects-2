# Copy here code of line function from previous exercise and use it in your solution
def line(num, string):
    if string == "":
        print("*"*int(num))
    else:
        print(string[0]*int(num))

def shape(size, char, size2, char2):
    i = 1
    j = 0
    while i <= size:
        line(i, char)
        i+=1
    while j < size2:
        line(size, char2)
        j+=1
    


# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 3, "*")
