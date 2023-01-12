from collections import deque
initial_string = input().split()
operations = {
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b,
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
}
numbers = deque()
for symbol in initial_string:
    if symbol in "+-*/":
        while len(numbers) > 1:
            left = numbers.popleft()
            right = numbers.popleft()
            result = operations[symbol](left, right)
            numbers.appendleft(result)
    else:
        numbers.append(int(symbol))
print(numbers[0])


