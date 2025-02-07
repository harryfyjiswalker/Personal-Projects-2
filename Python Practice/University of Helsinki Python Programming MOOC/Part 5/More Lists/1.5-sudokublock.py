def block_correct(sudoku: list, row_no: int, column_no: int):
    block = []
    counting = []
    evaluating = []
    for i in range(row_no, row_no+3):
        for j in range(column_no, column_no+3):
            block.append(sudoku[i][j]) 
    for k in range(1,10):
        m = block.count(k)
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
    
