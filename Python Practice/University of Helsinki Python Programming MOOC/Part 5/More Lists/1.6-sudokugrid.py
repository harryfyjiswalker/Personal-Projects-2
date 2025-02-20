def sudoku_grid_correct(sudoku:list):
    counting_rows = []
    evaluating_row = []
    columns =[]
    counting_col = []
    evaluating_col = []
    blocks = []
    counting_blo = []
    evaluating_blo = []
    #rows
    for a in range(len(sudoku)):
        counting_row = []
        for b in range(1,10):
            c = sudoku[a].count(b)
            counting_row.append(c)
        counting_rows.append(counting_row)
    for row in counting_rows:
        if any(x >= 2 for x in row):
            evaluating_row.append(1)
        else:
            evaluating_row.append(0)

    #columns
    for e in range(len(sudoku[0])):
        column = []
        for f in range(len(sudoku)):
            column.append(sudoku[f][e])
        columns.append(column)
    for column in columns:
        if any(column.count(g) >= 2 for g in range(1,10)):
            evaluating_col.append(1)
        else:
            evaluating_col.append(0)    
    
    #blocks

    for i in range(0, 7, 3):  
        for j in range(0, 7, 3):  
            block = []
            for k in range(i, i + 3):  
                for y in range(j, j + 3):  
                    block.append(sudoku[k][y])
            blocks.append(block)

    for block in blocks:
        if any(block.count(k) >= 2 for k in range(1, 10)):  
            evaluating_blo.append(1)
        else:
            evaluating_blo.append(0)

    if 1 in evaluating_row or 1 in evaluating_col or 1 in evaluating_blo:
        return False
    else:
        return True




# if __name__ == "__main__":
#     sudoku1 = [
#   [9, 0, 0],
#   [2, 0, 0],
#   [0, 2, 0],
# ]
#     print(sudoku_grid_correct(sudoku1))
