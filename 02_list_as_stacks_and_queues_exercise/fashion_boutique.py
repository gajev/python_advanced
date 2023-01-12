box_of_clothes = list(map(int, input().split()))
capacity = int(input())
sum_clothes = capacity
racks = 1
for current_item in reversed(box_of_clothes):
    if sum_clothes > current_item:
        sum_clothes -= current_item
    elif sum_clothes == current_item:
        sum_clothes = 0
    else:
        racks += 1
        sum_clothes = capacity - current_item
print(racks)

