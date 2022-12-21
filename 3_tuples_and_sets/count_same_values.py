numbers = tuple(map(float, input().split()))
unique_list = []
for current_number in numbers:
    if current_number not in unique_list:
        unique_list.append(current_number)
for number in unique_list:
    print(f'{number} - {numbers.count(number)} times')
