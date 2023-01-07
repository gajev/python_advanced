def next_position(row, col, direction):
    if direction == "left":
        return row, col - 1
    elif direction == "right":
        return row, col + 1
    elif direction == "up":
        return row - 1, col
    elif direction == "down":
        return row + 1, col


def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


presents = int(input())
size = int(input())
santa_row = 0
santa_col = 0
initial_good_kids = 0
good_kids = 0
matrix = []
for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == "S":
            santa_row, santa_col = row, col
        elif row_elements[col] == "V":
            initial_good_kids += 1
    matrix.append(row_elements)
while True:
    direction = input()
    if direction == "Christmas morning":
        break
    new_row, new_col = next_position(santa_row, santa_col, direction)
    if is_inside(new_row, new_col, size):
        matrix[santa_row][santa_col] = "-"
        if matrix[new_row][new_col] == "V":
            presents -= 1
            good_kids += 1
        elif matrix[new_row][new_col] == "C":
            if matrix[new_row + 1][new_col] == "V" or matrix[new_row + 1][new_col] == "X":
                presents -= 1
                if matrix[new_row + 1][new_col] == "V":
                    good_kids += 1
                matrix[new_row + 1][new_col] = "-"
                if presents == 0:
                    matrix[new_row][new_col] = "S"
                    break
            if matrix[new_row - 1][new_col] == "V" or matrix[new_row - 1][new_col] == "X":
                presents -= 1
                if matrix[new_row - 1][new_col] == "V":
                    good_kids += 1
                matrix[new_row - 1][new_col] = "-"
                if presents == 0:
                    matrix[new_row][new_col] = "S"
                    break
            if matrix[new_row][new_col + 1] == "V" or matrix[new_row][new_col + 1] == "X":
                presents -= 1
                if matrix[new_row][new_col + 1] == "V":
                    good_kids += 1
                matrix[new_row][new_col + 1] = "-"
                if presents == 0:
                    matrix[new_row][new_col] = "S"
                    break
            if matrix[new_row][new_col - 1] == "V" or matrix[new_row][new_col - 1] == "X":
                presents -= 1
                if matrix[new_row][new_col - 1] == "V":
                    good_kids += 1
                matrix[new_row][new_col - 1] = "-"
                if presents == 0:
                    matrix[new_row][new_col] = "S"
                    break
        matrix[new_row][new_col] = "S"
        santa_row, santa_col = new_row, new_col
    if presents == 0:
        break
if presents == 0 and initial_good_kids != good_kids:
    print("Santa ran out of presents!")
for current_row in matrix:
    print(*current_row, sep=" ")
if good_kids == initial_good_kids:
    print(f'Good job, Santa! {initial_good_kids} happy nice kid/s.')
else:
    print(f"No presents for {initial_good_kids - good_kids} nice kid/s.")
