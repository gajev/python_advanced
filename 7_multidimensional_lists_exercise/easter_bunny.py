size = int(input())
matrix = []
bunny_row = 0
bunny_col = 0
for row in range(size):
    current_col = input().split()
    for col in range(size):
        if current_col[col] == "B":
            bunny_col = int(col)
            bunny_row = int(row)
    matrix.append(current_col)
directions = {
    "left": lambda r, c: (r, c - 1),
    "right": lambda r, c: (r, c + 1),
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c)
}
max_sum = float("-inf")
path = []
correct_dir = ""
for direction in directions:
    temp_sum = 0
    temp_path = []
    row, col = directions[direction](bunny_row, bunny_col)
    while 0 <= row < size and 0 <= col < size and matrix[row][col] != "X":
        temp_sum += int(matrix[row][col])
        temp_path.append([row, col])
        row, col = directions[direction](row, col)
    if temp_sum > max_sum and temp_path:
        max_sum = temp_sum
        path = temp_path
        correct_dir = direction
print(correct_dir)
print(*path, sep="\n")
print(max_sum)




