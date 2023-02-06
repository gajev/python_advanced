def list_manipulator(numbers, command, place, *args):
    if command == "add":
        new_numbers = [int(x) for x in args]
        if place == "beginning":
            for number in reversed(new_numbers):
                numbers.insert(0, number)
        elif place == "end":
            for number in new_numbers:
                numbers.append(number)
    elif command == "remove":
        if place == "beginning":
            if not args:
                numbers.pop(0)
            else:
                for iteration in range(args[0]):
                    numbers.pop(0)
        if place == "end":
            if not args:
                numbers.pop()
            else:
                for iteration in range(args[0]):
                    numbers.pop()

    return numbers


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))