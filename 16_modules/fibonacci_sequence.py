from modules_package import fibonacci

while True:
    command = input().split()
    if command[0] == "Stop":
        break
    elif command[0] == "Create":
        count = int(command[2])
        fibonacci_list = fibonacci.create(count)
        print(*fibonacci_list)
    elif command[0] == "Locate":
        searched_index = int(command[1])
        # noinspection PyUnboundLocalVariable
        print(fibonacci.locate(searched_index, fibonacci_list))
