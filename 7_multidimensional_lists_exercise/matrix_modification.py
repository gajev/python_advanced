number = int(input())
matrix = []
for _ in range(number):
    matrix.append([int(x) for x in input().split()])
while True:
    command = input().split()
    if command[0] == "END":
        break
    row, col, value = int(command[1]), int(command[2]), int(command[3])
    if command[0] == "Add":
        if 0 <= row < len(matrix) and 0 <= col < len(matrix):
            matrix[row][col] += value
            continue
    else:
        if 0 <= row < len(matrix) and 0 <= col < len(matrix):
            matrix[row][col] -= value
            continue
    print("Invalid coordinates")
for current_row in matrix:
    print(*current_row, sep=" ")

