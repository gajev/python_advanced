from collections import deque


def check_gift(number):
    if number < 100:
        return "lower"
    elif 100 <= number < 200:
        return "Gemstone"
    elif 200 <= number < 300:
        return "Porcelain Sculpture"
    elif 300 <= number < 400:
        return "Gold"
    elif 400 <= number < 500:
        return "Diamond Jewellery"
    else:
        return "higher"


materials = [int(x) for x in input().split()]
magic_levels = deque(int(x) for x in input().split())
crafted_gifts = {}

while materials and magic_levels:
    current_material = materials.pop()
    current_magic_level = magic_levels.popleft()
    mix = current_material + current_magic_level
    current_gift = check_gift(mix)
    if current_gift == "lower" or current_gift == "higher":
        if current_gift == "lower":
            if mix % 2 == 0:
                mix = (2 * current_material) + (3 * current_magic_level)
            else:
                mix *= 2
        elif check_gift(mix) == "higher":
            mix /= 2
        if 100 <= mix < 500:
            current_gift = check_gift(mix)
        else:
            continue

    if current_gift not in crafted_gifts:
        crafted_gifts[current_gift] = 0
    crafted_gifts[current_gift] += 1

if "Gemstone" in crafted_gifts and "Porcelain Sculpture" in crafted_gifts or \
        "Gold" in crafted_gifts and "Diamond Jewellery" in crafted_gifts:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")
if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")

for present, quantity in sorted(crafted_gifts.items()):
    print(f"{present}: {quantity}")
