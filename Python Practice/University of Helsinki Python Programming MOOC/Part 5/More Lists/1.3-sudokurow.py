def row_correct(sudoku: list, row_no: int):
    counting = []
    evaluating = []
    row = sudoku[row_no]
    for k in range(1,10):
        m = row.count(k)
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
    

if __name__ == "__main__":
    s = [[9, 9, 0, 0, 8, 0, 3, 0, 0]]
    print(row_correct(s, 0))
