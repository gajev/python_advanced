from math import floor

def is_inside(row_inside, col_inside, row_size, col_size):
    return 0 <= row_inside < row_size and 0 <= col_inside < col_size


def get_next_position(x, y, direction, r, c):
    new_x = x
    new_y = y
    if direction == "up":
        new_x -= 1
        if not is_inside(new_x, new_y, r, c):
            new_x = r - 1
        return [new_x, new_y]
    if direction == "down":
        new_x += 1
        if not is_inside(new_x, new_y, r, c):
            new_x = 0
        return [new_x, new_y]
    if direction == "left":
        new_y -= 1
        if not is_inside(new_x, new_y, r, c):
            new_y = c - 1
        return [new_x, new_y]
    if direction == "right":
        new_y += 1
        if not is_inside(new_x, new_y, r, c):
            new_y = 0
        return [new_x, new_y]


n = int(input())
board = []
player_position = []
player_path = []
coins = 0
lost = False
for row in range(n):
    rows = [x for x in input().split()]
    board.append(rows)
    for col in range(n):
        if board[row][col] == "P":
            player_position.append(row)
            player_position.append(col)
            player_path.append([row, col])
            break

while True:
    if coins >= 100 or lost:
        break

    direction = input()
    board[player_position[0]][player_position[1]] = "0"
    next_position = get_next_position(player_position[0], player_position[1], direction, n, n)
    player_path.append(next_position)
    if board[next_position[0]][next_position[1]] == "X":
        lost = True
    else:
        coins += int(board[next_position[0]][next_position[1]])
        board[next_position[0]][next_position[1]] = "0"
        player_position[0] = next_position[0]
        player_position[1] = next_position[1]

if lost:
    print(f"Game over! You've collected {floor(coins / 2)} coins.")
else:
    print(f"You won! You've collected {coins} coins.")
print("Your path:")
for el in player_path:
    print(el)
