def chessboard(length):
    nums = ["0", "1"]

    for x in range(length):
        for y in range(length):
            i =  nums[(x + y + 1) % 2]
            print(i, end=(''))
        print()
    

# Testing the function
if __name__ == "__main__":
    chessboard(3)


#alternative sol:
def chessboard(size):
    i = 0
    while i < size:
        if i % 2 == 0:
            row = "10"*size
        else:
            row = "01"*size
        # Remove extra characters at the end of the row
        print(row[0:size])
        i += 1
 
