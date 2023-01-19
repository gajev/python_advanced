from collections import deque


def winner(matrix):
    rows, cols = 6, 7
    for row in range(rows - 1, -1, -1):
        for col in range(cols):
            if matrix[row][col] != "0":
                try:
                    if matrix[row][col] == matrix[row + 1][col] == matrix[row + 2][col] == matrix[row + 3][col]:
                        return True
                except IndexError:
                    pass
                try:
                    if matrix[row][col] == matrix[row][col + 1] == matrix[row][col + 2] == matrix[row][col + 3]:
                        return True
                except IndexError:
                    pass
                try:
                    if matrix[row][col] == matrix[row + 1][col + 1] == matrix[row + 2][col + 2] \
                            == matrix[row + 3][col + 3]:
                        return True
                except IndexError:
                    pass
                try:
                    if matrix[row][col] == matrix[row - 1][col + 1] == matrix[row - 2][col + 2] \
                            == matrix[row - 3][col + 3]:
                        return True
                except IndexError:
                    continue


board_rows, board_cols = 6, 7
board = []
player1_symbol, player2_symbol = 1, 2
player_symbols = deque([player1_symbol, player2_symbol])

for board_row in range(board_rows):
    board.append(["0"] * board_cols)
counter = 0
while True:
    if winner(board):
        break
    try:
        player_move = int(input(f"Player {player_symbols[0]}, please choose a column:"))
        if not 0 < player_move <= board_cols:
            print(f'Column must be between 1 and {board_cols}')
            continue
    except ValueError:
        print(f"Column must be a number between 1 and {board_cols}")
        continue

    for current_row in range(board_rows - 1, -1, -1):
        if board[current_row][player_move - 1] == "0":
            if player_symbols[0] == 1:
                board[current_row][player_move - 1] = "1"
            elif player_symbols[0] == 2:
                board[current_row][player_move - 1] = "2"
            player_symbols.append(player_symbols.popleft())
            counter += 1
            if winner(board):
                print(*board, sep="\n")
                print(f'The winner is player {player_symbols[1]}')
                break
            print(*board, sep="\n")
            if counter == 42:
                print("Draw!")
                quit()
            break
    else:
        print("No free space in the chosen column! Please, choose another one!")
