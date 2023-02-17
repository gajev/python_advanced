def get_next_position(x, y, direct):
    new_x = x
    new_y = y
    if direct == "up":
        new_x -= 1
    if direct == "down":
        new_x += 1
    if direct == "left":
        new_y -= 1
    if direct == "right":
        new_y += 1
    return [new_x, new_y]


n = int(input())
car = input()
board = []
tunnel1 = []
tunnel2 = []
finish = []
car_position = [0, 0]
kilometer_passed = 0
for rows in range(n):
    temp_list = input().split()
    board.append(temp_list)
    for cols in range(n):
        if board[rows][cols] == "T":
            if tunnel1:
                tunnel2.append(rows)
                tunnel2.append(cols)
            else:
                tunnel1.append(rows)
                tunnel1.append(cols)
        if board[rows][cols] == "F":
            finish.append(rows)
            finish.append(cols)

while True:
    direction = input()
    if direction == "End":
        board[car_position[0]][car_position[1]] = "C"
        print(f"Racing car {car} DNF.")
        break
    car_position = get_next_position(car_position[0], car_position[1], direction)
    if board[car_position[0]][car_position[1]] == "T":
        if car_position[0] == tunnel1[0] and car_position[1] == tunnel1[1]:
            car_position[0] = tunnel2[0]
            car_position[1] = tunnel2[1]
        else:
            car_position[0] = tunnel1[0]
            car_position[1] = tunnel1[1]
        board[tunnel1[0]][tunnel1[1]] = "."
        board[tunnel2[0]][tunnel2[1]] = "."
        kilometer_passed += 30
        continue
    elif board[car_position[0]][car_position[1]] == "F":
        board[car_position[0]][car_position[1]] = "C"
        print(f"Racing car {car} finished the stage!")
        kilometer_passed += 10
        break
    else:
        kilometer_passed += 10

print(f"Distance covered {kilometer_passed} km.")
for x in board:
    print("".join(x))


