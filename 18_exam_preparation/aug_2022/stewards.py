from collections import deque

seats = {x: x for x in input().split(", ")}
first = deque(int(x) for x in input().split(", "))
second = [int(x) for x in input().split(", ")]
seat_matches = []
rotations = 0

while True:
    current_seat_1 = ""
    current_seat_2 = ""
    current_first = first.popleft()
    current_second = second.pop()
    rotations += 1
    ascii_symbol = chr(current_first + current_second)
    current_seat_1 += str(current_first) + ascii_symbol
    current_seat_2 += str(current_second) + ascii_symbol
    for key, value in seats.items():
        if key == current_seat_1 or key == current_seat_2:
            if seats[key] != "taken":
                seats[key] = "taken"
                seat_matches.append(key)
            break
    else:
        first.append(current_first)
        second.insert(0, current_second)

    if len(seat_matches) == 3 or rotations == 10:
        break
print(f"Seat matches: {', '.join(x for x in seat_matches)}")
print(f"Rotations count: {rotations}")








