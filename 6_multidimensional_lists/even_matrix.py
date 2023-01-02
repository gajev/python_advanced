rows = int(input())
matrix = []
for _ in range(rows):
    even_list = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
    matrix.append(even_list)
print(matrix)