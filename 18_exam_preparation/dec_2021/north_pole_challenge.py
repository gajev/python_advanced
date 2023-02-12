def is_inside(row_inside, col_inside, row_size, col_size):
    return 0 <= row_inside < row_size and 0 <= col_inside < col_size


def get_next_position(x, y, direction, r, c):
    new_x = x
    new_y = y
    if direction == "up":
        new_x -= 1
        if not is_inside(new_x, new_y, r, c):
            new_x = r - 1
        return new_x, new_y
    if direction == "down":
        new_x += 1
        if not is_inside(new_x, new_y, r, c):
            new_x = 0
        return new_x, new_y
    if direction == "left":
        new_y -= 1
        if not is_inside(new_x, new_y, r, c):
            new_y = c - 1
        return new_x, new_y
    if direction == "right":
        new_y += 1
        if not is_inside(new_x, new_y, r, c):
            new_y = 0
        return new_x, new_y


def items_collected(row, col, current_board):
    for row_index in range(row):
        for col_index in range(col):
            if current_board[row_index][col_index] == "C" \
                or current_board[row_index][col_index] == "D" \
                    or current_board[row_index][col_index] == "G":
                return False
    return True


rows, cols = (int(x) for x in input().split(", "))
board = []
position = []
decorations = 0
gifts = 0
cookies = 0

for current_row in range(rows):
    temp_list = input().split()
    board.append(temp_list)
    for current_col in range(cols):
        if board[current_row][current_col] == "Y":
            position.append(current_row)
            position.append(current_col)

while True:
    command = input().split("-")
    if command[0] == "End":
        break
    current_direction = command[0]
    step = int(command[1])
    for current_move in range(step):
        board[position[0]][position[1]] = "x"
        next_position = get_next_position(position[0], position[1], current_direction, rows, cols)
        if board[next_position[0]][next_position[1]] == "C":
            cookies += 1
        elif board[next_position[0]][next_position[1]] == "D":
            decorations += 1
        elif board[next_position[0]][next_position[1]] == "G":
            gifts += 1
        board[next_position[0]][next_position[1]] = "Y"
        position[0] = next_position[0]
        position[1] = next_position[1]
        if items_collected(rows, cols, board):
            break
    if items_collected(rows, cols, board):
        print("Merry Christmas!")
        break


print("You've collected:")
print(f"- {decorations} Christmas decorations")
print(f"- {gifts} Gifts")
print(f"- {cookies} Cookies")
for i in board:
    print(" ".join(i))







