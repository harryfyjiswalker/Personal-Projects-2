def who_won(game_board: list):
    player1 = 0
    player2 = 0
    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            if game_board[i][j] == 0:
                continue
            if game_board[i][j] == 1:
                player1 += 1
            if game_board[i][j] == 2:
                player2 += 1
    if player1 > player2:
        return 1
    elif player2 > player1:
        return 2
    elif player2 == player1:
        return 0

if __name__ == "__main__":
    game_board = [[1, 2, 1], [0, 0, 1], [2, 1, 0]]
    print(who_won(game_board))
