rows, cols = (int(x) for x in input().split(", "))
matrix = []
sum_numbers = 0
for _ in range(rows):
    column = [int(x) for x in input().split(", ")]
    matrix.append(column)
    for number in column:
        sum_numbers += number
print(sum_numbers)
print(matrix)