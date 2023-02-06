from collections import deque

bomb_effect = deque(int(x) for x in input().split(", "))
bomb_casing = [int(x) for x in input().split(", ")]
bombs = {"Cherry Bombs": 0, "Datura Bombs": 0, "Smoke Decoy Bombs": 0}
bombs_values = {60: "Cherry Bombs", 40: "Datura Bombs", 120: "Smoke Decoy Bombs"}
bomb_pouch_filled = False
while bomb_effect and bomb_casing:
    if bombs["Cherry Bombs"] >= 3 and bombs["Datura Bombs"] >= 3 and bombs["Smoke Decoy Bombs"] >= 3:
        bomb_pouch_filled = True
        break
    current_effect = bomb_effect[0]
    current_casing = bomb_casing[-1]
    mix = current_casing + current_effect
    if mix in bombs_values:
        bombs[bombs_values[mix]] += 1
        bomb_effect.popleft()
        bomb_casing.pop()
    else:
        bomb_casing[-1] -= 5

if bomb_pouch_filled:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if bomb_effect:
    print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effect)}")
else:
    print("Bomb Effects: empty")
if bomb_casing:
    print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casing)}")
else:
    print("Bomb Casings: empty")

for bomb, quantity in sorted(bombs.items()):
    print(f"{bomb}: {quantity}")
