from collections import deque

players = deque(input().split(", "))
rest = deque([0, 0])
n = 6
board = []
exit_position = []
b_position = []
for rows in range(n):
    temp_list = input().split()
    board.append(temp_list)
    for cols in range(n):
        if board[rows][cols] == "E":
            exit_position.append(rows)
            exit_position.append(cols)

while True:
    current_player = players[0]
    current_move = input().split(", ")
    if rest[0] == 1:
        players.append(players.popleft())
        rest.append(rest.popleft() - 1)
        continue
    x = int(current_move[0].strip("("))
    y = int(current_move[1].strip(")"))
    if board[x][y] == "W":
        rest[0] = 1
        print(f"{current_player} hits a wall and needs to rest.")
    if board[x][y] == "T":
        print(f"{current_player} is out of the game! The winner is {players[1]}.")
        break
    if board[x][y] == "E":
        print(f"{current_player} found the Exit and wins the game!")
        break
    players.append(players.popleft())
    rest.append(rest.popleft())








