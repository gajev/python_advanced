def hits(matrix, row, col):
    moves = [
        [row - 2, col - 1],
        [row - 2, col + 1],
        [row - 1, col - 2],
        [row - 1, col + 2],
        [row + 1, col - 2],
        [row + 1, col + 2],
        [row + 2, col - 1],
        [row + 2, col + 1]
    ]
    result = 0
    for r, c in moves:
        if 0 <= r < len(matrix) and 0 <= c < len(matrix) and matrix[r][c] == "K":
            result += 1
    return result


size_of_board = int(input())
matrix = []
for _ in range(size_of_board):
    matrix.append(list(input()))
knights_removed = 0
while True:
    best_count = 0
    knight_row = 0
    knight_col = 0
    for row in range(size_of_board):
        for col in range(size_of_board):
            if matrix[row][col] != "K":
                continue
            number_of_hits = hits(matrix, row, col)
            if number_of_hits > best_count:
                best_count = number_of_hits
                knight_row = row
                knight_col = col
    if best_count == 0:
        break
    matrix[knight_row][knight_col] = "0"
    knights_removed += 1
print(knights_removed)
