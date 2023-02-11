### 71/100 ###

from collections import deque

males = [int(x) for x in input().split()]
females = deque(int(x) for x in input().split())
matches = 0

while males and females:
    current_male = males.pop()
    current_female = females.popleft()
    if current_female <= 0:
        males.append(current_male)
        continue
    if current_male <= 0:
        females.insert(0, current_female)
        continue
    if current_female % 25 == 0:
        if females:
            females.popleft()
        males.append(current_male)
        continue
    if current_male % 25 == 0:
        if males:
            males.pop()
        females.insert(0, current_female)
        continue

    if current_male == current_female:
        matches += 1
    else:
        males.append(current_male - 2)


print(f"Matches: {matches}")
if males:
    print(f"Males left: {', '.join(str(x) for x in reversed(males))}")
else:
    print("Males left: none")
if females:
    print(f"Females left: {', '.join(str(x) for x in females)}")
else:
    print("Females left: none")
