from collections import deque

caffeine = [int(x) for x in input().split(", ")]
energy_drink = deque(int(x) for x in input().split(", "))

max_sum = 300
caffeine_drank = 0

while caffeine and energy_drink:
    current_caffeine = caffeine.pop()
    current_energy_drink = energy_drink.popleft()
    mix = current_caffeine * current_energy_drink
    if mix + caffeine_drank <= max_sum:
        caffeine_drank += mix
    else:
        energy_drink.append(current_energy_drink)
        caffeine_drank -= 30
        if caffeine_drank < 0:
            caffeine_drank = 0

if energy_drink:
    print(f"Drinks left: {', '.join(str(x) for x in energy_drink)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {caffeine_drank} mg caffeine.")

