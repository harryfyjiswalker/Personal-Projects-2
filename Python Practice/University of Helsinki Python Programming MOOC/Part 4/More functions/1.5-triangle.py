# Copy here code of line function from previous exercise
def line(num, string):
    if string == "":
        print("*"*int(num))
    else:
        print(string[0]*int(num))

def triangle(size):
    i = 1
    while i <= size:
        line(i, "#")
        i+=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
