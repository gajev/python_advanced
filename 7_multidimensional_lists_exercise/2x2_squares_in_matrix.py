rows, cols = (int(x) for x in input().split())
matrix = []
squares = 0
for _ in range(rows):
    matrix.append([x for x in input().split()])
for i in range(rows - 1):
    for j in range(cols - 1):
        if matrix[i][j] == matrix[i][j + 1] == matrix[i + 1][j] == matrix[i + 1][j + 1]:
            squares += 1
print(squares)

