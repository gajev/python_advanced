from collections import deque


def math_operations(*args, **kwargs):
    numbers = deque(args)
    while numbers:
        current_number = numbers.popleft()
        kwargs["a"] += current_number
        if numbers:
            current_number = numbers.popleft()
            kwargs["s"] -= current_number
        if numbers:
            current_number = numbers.popleft()
            if current_number != 0:
                kwargs["d"] /= current_number
        if numbers:
            current_number = numbers.popleft()
            kwargs["m"] *= current_number
    sorted_dict = [f'{key}: {value:.1f}' for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))]
    return "\n".join(sorted_dict)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))

