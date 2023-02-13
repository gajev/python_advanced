from collections import deque

fireworks_effect = deque(int(x) for x in input().split(", "))
explosive_power = [int(x) for x in input().split(", ")]
fireworks_enough = False
palm = 0
willow = 0
crossette = 0

while fireworks_effect and explosive_power:
    current_effect = fireworks_effect.popleft()
    current_power = explosive_power.pop()
    if current_power <= 0:
        fireworks_effect.appendleft(current_effect)
        continue
    if current_effect <= 0:
        explosive_power.append(current_power)
        continue

    mix = current_effect + current_power

    if mix % 3 == 0 and mix % 5 != 0:
        palm += 1
    elif mix % 3 != 0 and mix % 5 == 0:
        willow += 1
    elif mix % 3 == 0 and mix % 5 == 0:
        crossette += 1
    else:
        fireworks_effect.append(current_effect - 1)
        explosive_power.append(current_power)
    if palm > 2 and willow > 2 and crossette > 2:
        fireworks_enough = True
        break

if fireworks_enough:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if fireworks_effect:
    print(f"Firework Effects left: {', '.join(str(x) for x in fireworks_effect)}")

if explosive_power:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_power)}")

print(f"Palm Fireworks: {palm}")
print(f"Willow Fireworks: {willow}")
print(f"Crossette Fireworks: {crossette}")
