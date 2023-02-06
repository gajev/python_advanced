def is_inside(row_inside, col_inside, size):
    return 0 <= row_inside < size and 0 <= col_inside < size


def next_position(row, col, matrix, direction):
    if direction == "up":
        return row - 1, col
    elif direction == "down":
        return row + 1, col
    elif direction == "left":
        return row, col - 1
    elif direction == "right":
        return row, col + 1


number = int(input())
board = []
player_position = tuple()
burrows = []
food = 0
win = False
for current_row in range(number):
    elements = input()
    board.append([el for el in elements])
    for current_col in range(number):
        if board[current_row][current_col] == "S":
            player_position = (current_row, current_col)
        elif board[current_row][current_col] == "B":
            burrows.append((current_row, current_col))
board[player_position[0]][player_position[1]] = "."
while True:
    current_move = input()
    player_position = next_position(player_position[0], player_position[1], board, current_move)
    if not is_inside(player_position[0], player_position[1], len(board)):
        break
    else:
        if board[player_position[0]][player_position[1]] == "B":
            for burrow in burrows:
                if burrow != (player_position[0], player_position[1]):
                    board[burrow[0]][burrow[1]] = "."
                    player_position = (burrow[0], burrow[1])
                else:
                    board[player_position[0]][player_position[1]] = "."
        elif board[player_position[0]][player_position[1]] == "*":
            food += 1
            if food == 10:
                win = True
                board[player_position[0]][player_position[1]] = "S"
                break
            else:
                board[player_position[0]][player_position[1]] = "."
        else:
            board[player_position[0]][player_position[1]] = "."

if win:
    board[player_position[0]][player_position[1]] = "S"
    print("You won! You fed the snake.")
else:
    print("Game over!")
print(f"Food eaten: {food}")
for row in board:
    print("".join(row))

