from collections import deque
petrol_pumps = int(input())
pumps = deque()
for _ in range(petrol_pumps):
    pumps.append([int(x) for x in input().split()])

for current_attempt in range(petrol_pumps):
    trunk = 0
    failed = False
    for petrol, distance in pumps:
        trunk += petrol - distance
        if trunk < 0:
            failed = True
            break
    if failed:
        pumps.append(pumps.popleft())
    else:
        print(current_attempt)
        break




