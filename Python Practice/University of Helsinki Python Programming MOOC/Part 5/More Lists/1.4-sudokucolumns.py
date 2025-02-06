def column_correct(sudoku: list, column_no: int):
    column = []
    counting = []
    evaluating = []
    for i in range(len(sudoku)):
        column.append(sudoku[i][column_no])
    for k in range(1,10):
        m = column.count(k)
        counting.append(m)
    for i in range(len(counting)):
        if counting[i] >= 2:
            evaluating.append(1)
        else:
            evaluating.append(0)      
    if 1 in evaluating:
        return False
    else:
        return True
    
