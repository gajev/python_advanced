from collections import deque

green_light = int(input())
free_window = int(input())
cars = deque()
cars_passed = 0
while True:
    command = input()
    if command == "END":
        break
    if command != "green":
        cars.append(command)
    elif command == "green":
        seconds_left = green_light
        while cars:
            seconds_needed = len(cars[0])
            if seconds_left == 0:
                break
            if seconds_left > seconds_needed:
                seconds_left -= seconds_needed
                cars_passed += 1
                cars.popleft()
            else:
                if seconds_left + free_window < len(cars[0]):
                    index = seconds_left + free_window
                    print("A crash happened!")
                    print(f"{cars[0]} was hit at {cars[0][index]}.")
                    quit()
                else:
                    cars_passed += 1
                    cars.popleft()
                    seconds_left = 0

print("Everyone is safe.")
print(f'{cars_passed} total cars passed the crossroads.')