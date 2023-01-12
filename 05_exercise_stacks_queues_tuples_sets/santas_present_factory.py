from collections import deque
materials = list(int(x) for x in input().split())
magic_level = deque(int(x) for x in input().split())
toys = {"Doll": 0, "Wooden train": 0, "Teddy bear": 0, "Bicycle": 0}
while magic_level and materials:
    material = materials.pop()
    magic = magic_level.popleft()
    if material == 0 and magic == 0:
        continue
    if material == 0:
        magic_level.appendleft(magic)
        continue
    if magic == 0:
        materials.append(material)
        continue
    result = material * magic
    if result == 150:
        toys["Doll"] += 1
    elif result == 250:
        toys["Wooden train"] += 1
    elif result == 300:
        toys["Teddy bear"] += 1
    elif result == 400:
        toys["Bicycle"] += 1
    elif result < 0:
        materials.append(material + magic)
    else:
        materials.append(material + 15)
if toys["Doll"] > 0 and toys["Wooden train"] > 0 or toys["Teddy bear"] > 0 and toys["Bicycle"] > 0:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f'Materials left: {", ".join(str(x) for x in reversed(materials))} ')
if magic_level:
    print(f'Magic left: {", ".join(str(x) for x in magic_level)} ')
for key, value in sorted(toys.items()):
    if value > 0:
        print(f'{key}: {value}')


