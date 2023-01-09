def even_odd(*args):
    command = args[-1]
    even_numbers = []
    odd_numbers = []
    for index in range(len(args) - 1):
        if args[index] % 2 == 0:
            even_numbers.append(args[index])
        else:
            odd_numbers.append(args[index])
    if command == "odd":
        return odd_numbers
    return even_numbers


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))