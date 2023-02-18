def get_next_position(x, y, direct):
    new_x = x
    new_y = y
    if direct == "up":
        new_x -= 1
    if direct == "down":
        new_x += 1
    if direct == "left":
        new_y -= 1
    if direct == "right":
        new_y += 1
    return [new_x, new_y]


n = int(input())
board = []
submarine_position = []
cruisers = 3
mines_hit = 0
for rows in range(n):
    temp_list = list(input())
    board.append(temp_list)
    for cols in range(n):
        if board[rows][cols] == "S":
            submarine_position.append(rows)
            submarine_position.append(cols)
board[submarine_position[0]][submarine_position[1]] = "-"
while True:
    current_direction = input()
    submarine_position = get_next_position(submarine_position[0], submarine_position[1], current_direction)
    if board[submarine_position[0]][submarine_position[1]] == "C":
        board[submarine_position[0]][submarine_position[1]] = "-"
        cruisers -= 1
        if cruisers == 0:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break
    elif board[submarine_position[0]][submarine_position[1]] == "*":
        board[submarine_position[0]][submarine_position[1]] = "-"
        mines_hit += 1
        if mines_hit == 3:
            print(f"Mission failed, U-9 disappeared! Last known coordinates"
                  f" [{submarine_position[0]}, {submarine_position[1]}]!")
            break

board[submarine_position[0]][submarine_position[1]] = "S"
for current_row in board:
    print("".join(x for x in current_row))