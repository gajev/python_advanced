rows, cols = (int(x) for x in input().split())
matrix = []
for i in range(97, 97 + rows):
    row = []
    for j in range(i, i + cols):
        row.append(chr(i) + chr(j) + chr(i))
    matrix.append(row)
for current_row in matrix:
    print(" ".join(current_row))


