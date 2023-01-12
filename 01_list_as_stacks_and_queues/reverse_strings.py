initial_string = list(input())
result = []
while len(initial_string) > 0:
    result.append(initial_string.pop())
print("".join(result))
