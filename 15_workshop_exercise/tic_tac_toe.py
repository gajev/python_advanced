from collections import deque


def winner():
    for r in range(3):
        for c in range(3):
            try:
                if players[0][1] == board[r][c] == board[r][c + 1] == board[r][c + 2]:
                    return True
            except IndexError:
                pass
            try:
                if players[0][1] == board[r][c] == board[r + 1][c] == board[r + 2][c]:
                    return True
            except IndexError:
                pass
    first_diagonal = all([board[i][i] == players[0][1] for i in range(3)])
    second_diagonal = all([board[i][2-i] == players[0][1] for i in range(3)])
    if first_diagonal or second_diagonal:
        return True


player_one = input("Player one name:")
player_two = input("Player two name:")
players = deque()
elements = ["O", "X"]
while True:
    player_one_symbol = input(f"{player_one} would you like to play with 'X' or 'O'?")
    if player_one_symbol != "X" and player_one_symbol != "O":
        print(f"{player_one} please select a valid symbol")
    else:
        break
player_two_symbol = "X" if player_one_symbol == "O" else "O"
players.append([player_one, player_one_symbol])
players.append([player_two, player_two_symbol])
board = [[str(i), str(i + 1), str(i + 2)] for i in range(1, 10, 3)]
print("This is the numeration of the board:")
[print(f"| {' | '.join(row)} |") for row in board]
print(f"{players[0][0]} starts first!")
counter = 0
while True:
    if winner():
        break
    current_move = input(f"{players[0][0]} choose a free position [1-9]:")
    if any([True if current_move in row else False for row in board]):
        row, col = (int(current_move) - 1) // 3, (int(current_move) - 1) % 3
        if board[row][col].isdigit():
            board[row][col] = players[0][1]
            [print(f"| {' | '.join([' ' if el not in elements else el for el in row])} |") for row in board]
            counter += 1
            if winner():
                print(f"{players[0][0]} won!")
                break
            if counter == 9:
                print("Draw!")
            players.append(players.popleft())
        else:
            print("This position is not free")
    else:
        print(f"{players[0][0]}, please select a valid position!")

