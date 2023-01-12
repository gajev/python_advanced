from collections import deque
working_bees = deque(int(x) for x in input().split())
nectar = list(int(x) for x in input().split())
operations_deque = deque(input().split())
operations = {
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
}
honey = 0
while nectar and working_bees:
    bee = working_bees.popleft()
    current_value = nectar.pop()
    if current_value < bee:
        working_bees.appendleft(bee)
        continue
    if current_value == 0:
        continue
    current_operation = operations_deque.popleft()
    honey += abs(operations[current_operation](bee, current_value))
print(f"Total honey made: {honey}")
if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
