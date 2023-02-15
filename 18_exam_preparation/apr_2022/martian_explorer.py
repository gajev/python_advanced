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

n = 6
board = []
rover_position = []
b_position = []
water = 0
concrete = 0
metal = 0
for rows in range(n):
    temp_list = input().split()
    board.append(temp_list)
    for cols in range(n):
        if board[rows][cols] == "E":
            rover_position.append(rows)
            rover_position.append(cols)

directions = input().split(", ")
for current_move in directions:
    rover_position = get_next_position(rover_position[0], rover_position[1], current_move, n, n)
    if board[rover_position[0]][rover_position[1]] == "W":
        board[rover_position[0]][rover_position[1]] = "-"
        print(f"Water deposit found at ({rover_position[0]}, {rover_position[1]})")
        water += 1
    if board[rover_position[0]][rover_position[1]] == "M":
        board[rover_position[0]][rover_position[1]] = "-"
        print(f"Metal deposit found at ({rover_position[0]}, {rover_position[1]})")
        metal += 1
    if board[rover_position[0]][rover_position[1]] == "C":
        board[rover_position[0]][rover_position[1]] = "-"
        print(f"Concrete deposit found at ({rover_position[0]}, {rover_position[1]})")
        concrete += 1
    if board[rover_position[0]][rover_position[1]] == "R":
        print(f"Rover got broken at ({rover_position[0]}, {rover_position[1]})")
        break
if water > 0 and concrete > 0 and metal > 0:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")



