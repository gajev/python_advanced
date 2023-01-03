rows, cols = (int(x) for x in input().split())
matrix = []
sum_square = float("-inf")
first_row = []
second_row = []
third_row = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split()])
for i in range(rows - 2):
    for j in range(cols - 2):
        result = matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2] + \
            matrix[i + 1][j] + matrix[i + 1][j + 1] + matrix[i + 1][j + 2] + \
            matrix[i + 2][j] + matrix[i + 2][j + 1] + matrix[i + 2][j + 2]
        if result > sum_square:
            sum_square = result
            first_row = [matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]]
            second_row = [matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]]
            third_row = [matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]]
print(f'Sum = {sum_square}')
print(*first_row)
print(*second_row)
print(*third_row)