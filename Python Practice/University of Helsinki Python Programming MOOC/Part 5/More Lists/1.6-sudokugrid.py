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
    for d in range(len(counting_row)):
        if counting_row[d] >= 2:
            evaluating_row.append(1)
        else:
            evaluating_row.append(0)

    #columns
    for e in range(len(sudoku[0])):
        column = []
        for f in range(len(sudoku)):
            column.append(sudoku[f][e])
        columns.append(column)
    for g in range(1,10):
        h = column.count(g)
        counting_col.append(h)
    for h in range(len(counting_col)):
        if counting_col[h] >= 2:
            evaluating_col.append(1)
        else:
            evaluating_col.append(0)      
    
    #blocks

    for i in range(0, 7):  
        for j in range(0, 7):  
            block = []
            for k in range(i, i+3):  
                for y in range(j, j+3):  
                    block.append(sudoku[x][y])
        blocks.append(block)

    for k in range(1,10):
        l = block.count(k)
        counting_blo.append(l)
    for m in range(len(counting_blo)):
        if counting_blo[i] >=2:
            evaluating_blo.append(1)
        else:
            evaluating_blo.append(0)
    
    if 1 in evaluating_row or 1 in evaluating_col or 1 in evaluating_blo:
        return False
    else:
        return True




if __name__ == "__main__":
    sudoku1 = [
  [9, 0, 0],
  [2, 0, 0],
  [0, 2, 0],
]
    print(sudoku_grid_correct(sudoku1))
