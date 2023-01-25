def is_inside(row_inside, col_inside, size):
    return 0 <= row_inside < size and 0 <= col_inside < size


n = int(input())
directions = input().split()
board = []
miner_position = []
end_of_route = []
total_coal = 0

for current_row in range(n):
    elements = input().split()
    board.append(elements)
    for current_col in range(n):
        if board[current_row][current_col] == "c":
            total_coal += 1
        elif board[current_row][current_col] == "e":
            end_of_route.append(current_row)
            end_of_route.append(current_col)
        elif board[current_row][current_col] == "s":
            miner_position.append(current_row)
            miner_position.append(current_col)

board[miner_position[0]][miner_position[1]] = "*"

for current_direction in directions:
    if current_direction == "up":
        if is_inside(miner_position[0] - 1, miner_position[1], len(board)):
            miner_position[0] -= 1
    elif current_direction == "down":
        if is_inside(miner_position[0] + 1, miner_position[1], len(board)):
            miner_position[0] += 1
    elif current_direction == "right":
        if is_inside(miner_position[0], miner_position[1] + 1, len(board)):
            miner_position[1] += 1
    elif current_direction == "left":
        if is_inside(miner_position[0], miner_position[1] - 1, len(board)):
            miner_position[1] -= 1

    if board[miner_position[0]][miner_position[1]] == "e":
        print(f"Game over! ({miner_position[0]}, {miner_position[1]})")
        break
    elif board[miner_position[0]][miner_position[1]] == "c":
        total_coal -= 1
        board[miner_position[0]][miner_position[1]] = "*"
        if total_coal == 0:
            print(f"You collected all coal! ({miner_position[0]}, {miner_position[1]})")
            break
else:
    print(f"{total_coal} pieces of coal left. ({miner_position[0]}, {miner_position[1]})")
