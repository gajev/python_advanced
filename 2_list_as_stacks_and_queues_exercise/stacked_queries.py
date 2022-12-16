number_of_commands = int(input())
stack = []
for current_query in range(number_of_commands):
    command = list(map(int, input().split()))
    if command[0] == 1:
        stack.append(command[1])
    elif command[0] == 2:
        if stack:
            stack.pop()
    elif command[0] == 3:
        if stack:
            print(max(stack))
    elif command[0] == 4:
        if stack:
            print(min(stack))
print(*reversed(stack), sep=", ")