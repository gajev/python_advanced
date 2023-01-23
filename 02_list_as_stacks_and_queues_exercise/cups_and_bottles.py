from collections import deque

cups = deque(int(x) for x in input().split())
bottles = [int(x) for x in input().split()]
wasted_water = 0
while cups and bottles:
    temp_sum = bottles.pop() if bottles[-1] >= cups[0] else 0
    while temp_sum < cups[0]:
        temp_sum += bottles.pop()
    wasted_water += temp_sum - cups.popleft()
if bottles:
    print(f'Bottles: {" ".join(str(x) for x in bottles)}')
else:
    print(f'Cups: {" ".join(str(x) for x in cups)}')
print(f'Wasted litters of water: {wasted_water}')
