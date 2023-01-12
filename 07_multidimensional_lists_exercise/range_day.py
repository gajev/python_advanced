def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


def next_position(row, col, direction, steps):
    if direction == "left":
        return row, col - steps
    elif direction == "right":
        return row, col + steps
    elif direction == "up":
        return row - steps, col
    elif direction == "down":
        return row + steps, col


size = 5
player_row = 0
player_col = 0
matrix = []
targets_count = 0
hit_targets = []
for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == "A":
            player_row = row
            player_col = col
        elif row_elements[col] == "x":
            targets_count += 1
    matrix.append(row_elements)
matrix[player_row][player_col] = "."


number_of_commands = int(input())
for _ in range(number_of_commands):
    current_command = input().split()
    command = current_command[0]
    direction = current_command[1]
    if command == "move":
        steps = int(current_command[2])
        new_row, new_col = next_position(player_row, player_col, direction, steps)
        if is_inside(new_row, new_col, size) and matrix[new_row][new_col] == ".":
            player_row, player_col = new_row, new_col
    else:
        bullet_row, bullet_col = next_position(player_row, player_col, direction, 1)
        while is_inside(bullet_row, bullet_col, size):
            if matrix[bullet_row][bullet_col] == "x":
                matrix[bullet_row][bullet_col] = "."
                targets_count -= 1
                hit_targets.append([bullet_row, bullet_col])
                break
            bullet_row, bullet_col = next_position(bullet_row, bullet_col, direction, 1)
        if targets_count == 0:
            break
if targets_count == 0:
    print(f'Training completed! All {len(hit_targets)} targets hit.')
else:
    print(f'Training not completed! {targets_count} targets left.')
print(*hit_targets, sep="\n")
