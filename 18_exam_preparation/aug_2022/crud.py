def get_next_position(x, y, direction):
    new_x = x
    new_y = y
    if direction == "up":
        new_x -= 1
    if direction == "down":
        new_x += 1
    if direction == "left":
        new_y -= 1
    if direction == "right":
        new_y += 1
    return [new_x, new_y]


board = []
position = []
for rows in range(6):
    temp_list = input().split()
    board.append(temp_list)
x1, y1 = input().split(", ")
position.append(int(x1.strip("(")))
position.append(int(y1.strip(")")))

while True:
    command = input().split(", ")
    action = command[0]
    if action == "Stop":
        break
    current_direction = command[1]
    if action == "Create":
        value = command[2]
        position = get_next_position(position[0], position[1], current_direction)
        if board[position[0]][position[1]] == ".":
            board[position[0]][position[1]] = value
    elif action == "Update":
        update_value = command[2]
        position = get_next_position(position[0], position[1], current_direction)
        if board[position[0]][position[1]] != ".":
            board[position[0]][position[1]] = update_value
    elif action == "Delete":
        position = get_next_position(position[0], position[1], current_direction)
        if board[position[0]][position[1]] != ".":
            board[position[0]][position[1]] = "."
    elif action == "Read":
        position = get_next_position(position[0], position[1], current_direction)
        if board[position[0]][position[1]] != ".":
            print(board[position[0]][position[1]])

for row in board:
    print(" ".join(row))


