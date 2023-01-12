rows = int(input())
matrix = []
diagonal = 0
for _ in range(rows):
    matrix.append([int(x) for x in input().split()])
for i in range(rows):
    diagonal += matrix[i][i]
print(diagonal)