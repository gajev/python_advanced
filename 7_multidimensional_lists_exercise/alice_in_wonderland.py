size = int(input())
matrix = []
alice_row = 0
alice_col = 0
for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == "A":
            alice_row = int(row)
            alice_col = int(col)
    matrix.append(row_elements)
tea_bags = 0
while tea_bags < 10:
    matrix[alice_row][alice_col] = "*"
    direction = input()
    if direction == "left":
        alice_col -= 1
    elif direction == "right":
        alice_col += 1
    elif direction == "up":
        alice_row -= 1
    elif direction == "down":
        alice_row += 1
    if not 0 <= alice_row < size or not 0 <= alice_col < size:
        break
    if matrix[alice_row][alice_col] == "R":
        matrix[alice_row][alice_col] = "*"
        break
    if matrix[alice_row][alice_col] == "." or matrix[alice_row][alice_col] == "*":
        continue
    tea_bags += int(matrix[alice_row][alice_col])
if tea_bags < 10:
    print("Alice didn't make it to the tea party.")
else:
    matrix[alice_row][alice_col] = "*"
    print("She did it! She went to the party.")
for current_row in matrix:
    print(*current_row, sep=" ")
