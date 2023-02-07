def numbers_searching(*args):
    min_number = min(args)
    max_number = max(args)
    missing_number = 0
    result = []
    duplicates = {}
    duplicates_list = []
    for current_number in range(min_number, max_number + 1):
        if current_number not in args:
            missing_number = current_number
    for number in args:
        if number not in duplicates:
            duplicates[number] = 0
        duplicates[number] += 1
    for key, value in duplicates.items():
        if value > 1:
            duplicates_list.append(key)

    result.append(missing_number)
    result.append(sorted(duplicates_list))
    return result


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))