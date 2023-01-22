def create(number):
    list_numbers = [0, 1]
    if number == 1:
        return 0
    elif number == 2:
        return "0 1"
    else:
        for i in range(3, number + 1):
            current_number = list_numbers[-1] + list_numbers[-2]
            list_numbers.append(current_number)
    return list_numbers


def locate(target, nums):
    for index in range(len(nums)):
        current_num = nums[index]
        if current_num == target:
            return f"The number - {target} is at index {index}"
    return f"The number {target} is not in the sequence"


