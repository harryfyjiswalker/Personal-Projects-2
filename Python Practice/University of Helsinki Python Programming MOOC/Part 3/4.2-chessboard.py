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
