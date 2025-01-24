# Copy here code of line function from previous exercise
def line(num, string):
    if string == "":
        print("*"*int(num))
    else:
        print(string[0]*int(num))
    
def box_of_hashes(height):
    i = 0
    while i < height:
        line(10, "#")
        i += 1
    


# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
