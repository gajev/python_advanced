from collections import deque

elves = deque([int(x) for x in input().split()])
materials = [int(x) for x in input().split()]
total_energy = 0
toys = 0
counter = 0

while elves and materials:
    current_elf = elves.popleft()
    current_material = materials.pop()
    counter += 1
    if current_elf < 5:
        materials.append(current_material)
        counter -= 1
        continue

    if counter % 3 == 0:
        if current_elf >= 2 * current_material:
            current_elf -= 2 * current_material
            elves.append(current_elf + 1)
            toys += 2
            total_energy += 2 * current_material
            if counter % 5 == 0:
                elves[-1] -= 1
                toys -= 2
            continue
        else:
            elves.append(current_elf * 2)
            materials.append(current_material)
            continue

    if current_elf >= current_material:
        current_elf -= current_material
        toys += 1
        elves.append(current_elf + 1)
        total_energy += current_material
    else:
        elves.append(2 * current_elf)
        materials.append(current_material)
        continue

    if counter % 5 == 0:
        toys -= 1
        elves[-1] -= 1


print(f"Toys: {toys}")
print(f"Energy: {total_energy}")
if elves:
    print(f"Elves left: {', '.join(str(x) for x in elves)}")
if materials:
    print(f"Boxes left: {', '.join(str(x) for x in materials)}")
