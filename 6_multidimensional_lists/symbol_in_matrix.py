rows = int(input())
matrix = []
for _ in range(rows):
    matrix.append([ch for ch in input()])

searched_symbol = input()
for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        if searched_symbol == matrix[row][column]:
            print(f'({row}, {column})')
            quit()
print(f"{searched_symbol} does not occur in the matrix")
