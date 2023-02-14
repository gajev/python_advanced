def is_inside(r, c, n):
    return 0 <= r < n and 0 <= c < n


def attack(row, col, turn, matrix):
    if turn == "w":
        if is_inside(row - 1, col - 1, 8):
            if matrix[row - 1][col - 1] == "b":
                return True
        if is_inside(row - 1, col + 1, 8):
            if matrix[row - 1][col + 1] == "b":
                return True

    elif turn == "b":
        if is_inside(row + 1, col - 1, 8):
            if matrix[row + 1][col - 1] == "w":
                return True
        if is_inside(row + 1, col + 1, 8):
            if matrix[row + 1][col + 1] == "w":
                return True


def square(x, y):
    letter = {}
    digit = {}
    ascii_first = 97
    number = 8
    for i in range(8):
        letter[i] = chr(ascii_first)
        ascii_first += 1
        digit[i] = number
        number -= 1
    result = letter[y] + str(digit[x])
    return result


board = []
w_position = []
b_position = []
for rows in range(8):
    temp_list = input().split()
    board.append(temp_list)
    for cols in range(8):
        if board[rows][cols] == "w":
            w_position.append(rows)
            w_position.append(cols)
        if board[rows][cols] == "b":
            b_position.append(rows)
            b_position.append(cols)

while True:
    if attack(w_position[0], w_position[1], "w", board):
        print(f"Game over! White win, capture on {square(b_position[0], b_position[1])}.")
        break
    w_position[0] -= 1
    board[w_position[0]][w_position[1]] = "w"
    if w_position[0] == 0:
        print(f"Game over! White pawn is promoted to a queen at {square(w_position[0], w_position[1])}.")
        break

    if attack(b_position[0], b_position[1], "b", board):
        print(f"Game over! Black win, capture on {square(w_position[0], w_position[1])}.")
        break
    b_position[0] += 1
    board[b_position[0]][b_position[1]] = "b"
    if b_position[0] == 7:
        print(f"Game over! Black pawn is promoted to a queen at {square(b_position[0], b_position[1])}.")
        break

