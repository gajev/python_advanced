from collections import deque
from math import ceil

def is_inside(row_inside, col_inside, size):
    return 0 <= row_inside < size and 0 <= col_inside < size


def count_points(x, y, letter, matrix):
    sum_elements = 0
    sum_elements += int(board[x][0])
    sum_elements += int(board[x][6])
    sum_elements += int(board[0][y])
    sum_elements += int(board[6][y])
    if letter == "D":
        return sum_elements * 2
    elif letter == "T":
        return sum_elements * 3


players = deque(x for x in input().split(", "))
throws_counter = 0
board = []
players_score = deque([501, 501])

for row in range(7):
    current_row = [x for x in input().split()]
    board.append(current_row)

while True:
    current_throw = input().split(", ")
    first = int(current_throw[0].strip("("))
    second = int(current_throw[1].strip(")"))
    throws_counter += 1
    if is_inside(first, second, 7):
        if board[first][second] == "D":
            score = count_points(first, second, "D", board)
        elif board[first][second] == "T":
            score = count_points(first, second, "T", board)
        elif board[first][second] == "B":
            break
        else:
            score = int(board[first][second])
        players_score[0] -= score
    if players_score[0] <= 0:
        break
    players_score.append(players_score.popleft())
    players.append(players.popleft())

print(f"{players.popleft()} won the game with {ceil(throws_counter/2)} throws!")



