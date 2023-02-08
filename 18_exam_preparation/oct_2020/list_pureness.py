def best_list_pureness(list_of_numbers, k):
    temp_list = list_of_numbers
    pureness = 0
    rotation = 0
    for current_rotation in range(k + 1):
        temp_pureness = 0
        for number, index in enumerate(temp_list):
            temp_pureness += number * index
        if temp_pureness > pureness:
            pureness = temp_pureness
            rotation = current_rotation
        temp_list.insert(0, temp_list[-1])
        temp_list = temp_list[:-1]
    return f"Best pureness {pureness} after {rotation} rotations"


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
