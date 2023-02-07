def is_inside(row_inside, col_inside, size):
    return 0 <= row_inside < size and 0 <= col_inside < size


def mines_number(r, c, matrix):
    number = 0
    if is_inside(r - 1, c - 1, len(matrix)) and matrix[r - 1][c - 1] == "*":
        number += 1
    if is_inside(r - 1, c, len(matrix)) and matrix[r - 1][c] == "*":
        number += 1
    if is_inside(r - 1, c + 1, len(matrix)) and matrix[r - 1][c + 1] == "*":
        number += 1
    if is_inside(r, c - 1, len(matrix)) and matrix[r][c - 1] == "*":
        number += 1
    if is_inside(r, c + 1, len(matrix)) and matrix[r][c + 1] == "*":
        number += 1
    if is_inside(r + 1, c - 1, len(matrix)) and matrix[r + 1][c - 1] == "*":
        number += 1
    if is_inside(r + 1, c, len(matrix)) and matrix[r + 1][c] == "*":
        number += 1
    if is_inside(r + 1, c + 1, len(matrix)) and matrix[r + 1][c + 1] == "*":
        number += 1
    return number


n = int(input())
number_of_bombs = int(input())
bomb_coordinates = []
for initial_coordinates in range(number_of_bombs):
    coordinates = input().split(", ")
    first, second = int(coordinates[0].strip("(")), int(coordinates[-1].strip(")"))
    bomb_coordinates.append(first)
    bomb_coordinates.append(second)

board = []
for row in range(n):
    rows = []
    for col in range(n):
        rows.append("-")
    board.append(rows)
while bomb_coordinates:
    x = bomb_coordinates.pop(0)
    y = bomb_coordinates.pop(0)
    if is_inside(x, y, len(board)):
        board[x][y] = "*"
for i in range(n):
    for j in range(n):
        if board[i][j] != "*":
            board[i][j] = mines_number(i, j, board)

for _ in range(n):
    print(" ".join(str(x) for x in board[_]))
