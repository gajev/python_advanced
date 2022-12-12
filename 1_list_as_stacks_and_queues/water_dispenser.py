from collections import deque
quantity_of_water = int(input())
q = deque()
command = input()
while command != "Start":
    q.append(command)
    command = input()
new_command = input().split()
while new_command[0] != "End":
    if new_command[0] == "refill":
        quantity_of_water += int(new_command[1])
    else:
        if int(new_command[0]) <= quantity_of_water:
            quantity_of_water -= int(new_command[0])
            print(f'{q.popleft()} got water')
        else:
            print(f'{q.popleft()} must wait')
    new_command = input().split()
print(f'{quantity_of_water} liters left')
