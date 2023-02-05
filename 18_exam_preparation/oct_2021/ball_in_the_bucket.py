def is_inside(row_inside, col_inside, size):
    return 0 <= row_inside < size and 0 <= col_inside < size


board = [[int(x) if x[-1].isdigit() else x for x in input().split()] for row in range(6)]
points = 0

for current_throw in range(3):
    coordinates = input().split(", ")
    x, y = int(coordinates[0].strip("(")), int(coordinates[-1].strip(")"))
    if is_inside(x, y, 6):
        if board[x][y] == "B":
            for row in range(6):
                if board[row][y] != "B":
                    points += board[row][y]
                else:
                    board[row][y] = 0

if points < 100:
    needed_points = 100 - points
    print(f"Sorry! You need {needed_points} points more to win a prize.")
elif 100 <= points < 200:
    print(f"Good job! You scored {points} points, and you've won Football.")
elif 200 <= points < 300:
    print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
else:
    print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")