def is_inside(row_inside, col_inside, size):
    return 0 <= row_inside < size and 0 <= col_inside < size


def queen_coordinates(king_row, king_col, matrix):
    all_queens = []
    while is_inside(king_row, king_col, len(matrix)):
        queen = []
        if is_inside(king_row + 1, king_col, 8) and matrix[king_row + 1][king_col] == "Q":
            queen.append(king_row + 1)
            queen.append(king_col)
            all_queens.append(queen)
            break
        king_row += 1
    king_row, king_col = king_position[0], king_position[1]

    while is_inside(king_row, king_col, len(matrix)):
        queen = []
        if is_inside(king_row + 1, king_col - 1, 8) and matrix[king_row + 1][king_col - 1] == "Q":
            queen.append(king_row + 1)
            queen.append(king_col - 1)
            all_queens.append(queen)
            break
        king_row += 1
        king_col -= 1
    king_row, king_col = king_position[0], king_position[1]

    while is_inside(king_row, king_col, len(matrix)):
        queen = []
        if is_inside(king_row + 1, king_col + 1, 8) and matrix[king_row + 1][king_col + 1] == "Q":
            queen.append(king_row + 1)
            queen.append(king_col + 1)
            all_queens.append(queen)
            break
        king_row += 1
        king_col += 1
    king_row, king_col = king_position[0], king_position[1]

    while is_inside(king_row, king_col, len(matrix)):
        queen = []
        if is_inside(king_row, king_col - 1, 8) and matrix[king_row][king_col - 1] == "Q":
            queen.append(king_row)
            queen.append(king_col - 1)
            all_queens.append(queen)
            break
        king_col -= 1
    king_row, king_col = king_position[0], king_position[1]

    while is_inside(king_row, king_col, len(matrix)):
        queen = []
        if is_inside(king_row, king_col + 1, 8) and matrix[king_row][king_col + 1] == "Q":
            queen.append(king_row)
            queen.append(king_col + 1)
            all_queens.append(queen)
            break
        king_col += 1
    king_row, king_col = king_position[0], king_position[1]

    while is_inside(king_row, king_col, len(matrix)):
        queen = []
        if is_inside(king_row - 1, king_col, 8) and matrix[king_row - 1][king_col] == "Q":
            queen.append(king_row - 1)
            queen.append(king_col)
            all_queens.append(queen)
            break
        king_row -= 1
    king_row, king_col = king_position[0], king_position[1]

    while is_inside(king_row, king_col, len(matrix)):
        queen = []
        if is_inside(king_row - 1, king_col - 1, 8) and matrix[king_row - 1][king_col - 1] == "Q":
            queen.append(king_row - 1)
            queen.append(king_col - 1)
            all_queens.append(queen)
            break
        king_row -= 1
        king_col -= 1
    king_row, king_col = king_position[0], king_position[1]

    while is_inside(king_row, king_col, len(matrix)):
        queen = []
        if is_inside(king_row - 1, king_col + 1, 8) and matrix[king_row - 1][king_col + 1] == "Q":
            queen.append(king_row - 1)
            queen.append(king_col + 1)
            all_queens.append(queen)
            break
        king_row -= 1
        king_col += 1

    return all_queens


board = []
king_position = []
for row in range(8):
    rows = [x for x in input().split()]
    board.append(rows)
    for col in range(8):
        if board[row][col] == "K":
            king_position.append(row)
            king_position.append(col)
            break


queens = queen_coordinates(king_position[0], king_position[1], board)
if not queens:
    print("The king is safe!")
else:
    print(*queens, sep="\n")
