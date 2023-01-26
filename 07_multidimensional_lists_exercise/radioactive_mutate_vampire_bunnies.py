rows, cols = [int(x) for x in input().split()]
board = [list(input()) for row in range(rows)]
print(board)
directions = input()
player_position = ()

for current_row in range(rows):
    for current_col in range(cols):
        if board[current_row][current_col] == "P":
            player_position = (current_row, current_col)

directions_dict = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0)
}

won = False
dead = False

for direction in directions:
    board[player_position[0]][player_position[1]] = "."
    next_x, next_y = directions_dict[direction]
    next_x_p, next_y_p = player_position[0] + next_x, player_position[1] + next_y
    if 0 <= next_x_p < rows and 0 <= next_y_p < cols:
        player_position = (next_x_p, next_y_p)
        if board[next_x_p][next_y_p] == "B":
            dead = True
        else:
            board[next_x_p][next_y_p] = "P"
    else:
        won = True
    bunnies_positions = []
    for current_row in range(rows):
        for current_col in range(cols):
            if board[current_row][current_col] == "B":
                bunny_position = (current_row, current_col)
                for direct in directions_dict:
                    bunny_first_index, bunny_second_index = directions_dict[direct]
                    new_bunny_first_index, new_bunny_second_index = bunny_position[0] + bunny_first_index, \
                        bunny_position[1] + bunny_second_index
                    if 0 <= new_bunny_first_index < rows and 0 <= new_bunny_second_index < cols:
                        bunnies_positions.append((new_bunny_first_index, new_bunny_second_index))
    for bunny in bunnies_positions:
        if board[bunny[0]][bunny[1]] == "P":
            dead = True
        board[bunny[0]][bunny[1]] = "B"
    if dead:
        break
    if won:
        break

for row in board:
    print(f"{''.join(row)}")

if dead:
    print(f"dead: {' '.join(str(x) for x in player_position)}")
if won:
    print(f"won: {' '.join(str(x) for x in player_position)}")
