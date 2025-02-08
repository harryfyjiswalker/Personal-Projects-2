def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_list =[]
    for item in sudoku:
        new_list.append(item[:]) #need this to create completely new list, else just directing to same list
    if sudoku[row_no][column_no] != number:
        new_list[row_no][column_no] = number
    return new_list

