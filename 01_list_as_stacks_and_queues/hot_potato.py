from collections import deque
kids = deque(input().split())
number = int(input())
counter = 1
while len(kids) > 1:
    current_kid = kids.popleft()
    if counter == number:
        print(f'Removed {current_kid}')
        counter = 1
    else:
        counter += 1
        kids.append(current_kid)
winner = kids.popleft()
print(f'Last is {winner}')