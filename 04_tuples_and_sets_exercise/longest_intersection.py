number_of_lines = int(input())
longest_intersection = set()
for _ in range(number_of_lines):
    ranges = input().split("-")
    first_range = ranges[0].split(",")
    second_range = ranges[1].split(",")
    left_part = set()
    right_part = set()
    for number in range(int(first_range[0]), int(first_range[1]) + 1):
        left_part.add(number)
    for second_number in range(int(second_range[0]), int(second_range[1]) + 1):
        right_part.add(second_number)
    current_intersection = left_part.intersection(right_part)
    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection
longest_intersection_list = [i for i in longest_intersection]
print(f"Longest intersection is {longest_intersection_list} with length {len(longest_intersection_list)}")
