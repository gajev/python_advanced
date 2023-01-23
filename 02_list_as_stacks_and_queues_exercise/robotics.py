from collections import deque


def time(time_seconds):
    h = time_seconds // 3600
    m = (time_seconds % 3600) // 60
    s = (time_seconds % 3600) % 60
    return f'{h:02d}:{m:02d}:{s:02d}'


def products():
    result = deque()
    while True:
        current_product = input()
        if current_product == "End":
            break
        result.append(current_product)
    return result


initial_robots = input().split(";")

free_robots = {}
busy_robots = {}

for element in initial_robots:
    robot, seconds = element.split("-")
    free_robots[robot] = int(seconds)

initial_time = input().split(":")
time_in_seconds = int(initial_time[0]) * 3600 + int(initial_time[1]) * 60 + int(initial_time[2])
items = products()

while items:
    time_in_seconds = (time_in_seconds + 1) % (24 * 60 * 60)
    for robot_name in [name for name in busy_robots.keys()]:
        busy_robots[robot_name] -= 1
        if busy_robots[robot_name] <= 0:
            busy_robots.pop(robot_name)
    for free_robot, seconds_left in free_robots.items():
        if free_robot not in busy_robots:
            busy_robots[free_robot] = seconds_left
            print(f'{free_robot} - {items.popleft()} [{time(time_in_seconds)}]')
            break
    else:
        items.append(items.popleft())


