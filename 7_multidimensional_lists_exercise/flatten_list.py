initial_numbers = input().strip().split("|")
final_list = []
for index in range(len(initial_numbers) - 1, -1, -1):
    current_list = initial_numbers[index].strip().split()
    final_list.extend(current_list)
print(*final_list)