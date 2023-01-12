set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))
first_numbers = []
second_numbers = []
for current_number in set1:
    first_numbers.append(current_number)
for current_number in set2:
    second_numbers.append(current_number)
number_of_commands = int(input())
for current_command in range(number_of_commands):
    command = input().split()
    action = command[0]
    if action == "Add":
        if command[1] == "First":
            for number in command:
                if number.isdigit() and int(number) not in first_numbers:
                    first_numbers.append(int(number))
        elif command[1] == "Second":
            for number in command:
                if number.isdigit() and int(number) not in second_numbers:
                    second_numbers.append(int(number))
    elif action == "Remove":
        if command[1] == "First":
            for number in command:
                if number.isdigit() and int(number) in first_numbers:
                    first_numbers.remove(int(number))
        elif command[1] == "Second":
            for number in command:
                if number.isdigit() and int(number) in second_numbers:
                    second_numbers.remove(int(number))
    elif action == "Check":
        if set(first_numbers).issubset(set(second_numbers)) or set(second_numbers).issubset(set(first_numbers)):
            print("True")
        else:
            print("False")
print(*sorted(first_numbers), sep=", ")
print(*sorted(second_numbers), sep=", ")