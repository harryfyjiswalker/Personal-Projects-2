def print_sudoku(sudoku: list):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            if sudoku[i][j] == 0:
                print("_", end=" ")  # print "_" instead of 0
            else:
                print(sudoku[i][j], end=" ")  # print the number
            if i == 2 and j == 8 or i == 5 and j == 8:
                print()
            if j % 3 == 2 and j != 8:
                print(" ", end="")
        print() 

def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number
    
