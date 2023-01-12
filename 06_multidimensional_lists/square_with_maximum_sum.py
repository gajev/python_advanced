rows, cols = (int(x) for x in input().split(", "))
matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split(", ")])
first_two = []
second_two = []
total = 0
for row in range(rows - 1):
    for index in range(cols - 1):
        sum_square = matrix[row][index] + matrix[row + 1][index] + matrix[row][index + 1] + matrix[row + 1][index + 1]
        if sum_square > total:
            total = sum_square
            first_two = [matrix[row][index], matrix[row][index + 1]]
            second_two = [matrix[row + 1][index], matrix[row + 1][index + 1]]
result = sum(first_two) + sum(second_two)
print(*first_two)
print(*second_two)
print(result)