def next_position(x, y, direction):
    if direction == "up":
        x -= 1
    if direction == "down":
        x += 1
    if direction == "left":
        y -= 1
    if direction == "right":
        y += 1
    return x, y


def is_inside(row_inside, col_inside, size):
    return 0 <= row_inside < size and 0 <= col_inside < size


word = input()
n = int(input())
board = []
player_position = tuple

for current_row in range(n):
    elements = input()
    board.append([el for el in elements])
    for current_col in range(n):
        if board[current_row][current_col] == "P":
            player_position = (current_row, current_col)
m = int(input())
for move in range(m):
    current_move = input()
    player_next_position = next_position(player_position[0], player_position[1], current_move)
    if is_inside(player_next_position[0], player_next_position[1], len(board)):
        symbol = board[player_next_position[0]][player_next_position[1]]
        if symbol.isalpha():
            word += symbol
        board[player_next_position[0]][player_next_position[1]] = "P"
        board[player_position[0]][player_position[1]] = "-"
        player_position = player_next_position
    else:
        if word:
            word = word[:-1]

print(word)
for row in board:
    print("".join(row))


