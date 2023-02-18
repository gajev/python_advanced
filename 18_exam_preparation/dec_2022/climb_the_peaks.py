from collections import deque

daily_food = [int(x) for x in input().split(", ")]
stamina = deque(int(x) for x in input().split(", "))
peaks = {80: "Vihren", 90: "Kutelo", 100: "Banski Suhodol", 60: "Polezhan", 70: "Kamenitza"}
peaks_difficulty_level = deque([80, 90, 100, 60, 70])
conquered = []

for current_day in range(7):
    if not peaks_difficulty_level or not daily_food or not stamina:
        break
    current_food = daily_food.pop()
    current_stamina = stamina.popleft()
    mix = current_stamina + current_food
    if mix >= peaks_difficulty_level[0]:
        conquered.append(peaks[peaks_difficulty_level.popleft()])


if len(conquered) == 5:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
if conquered:
    print("Conquered peaks:")
    print('\n'.join(x for x in conquered))


