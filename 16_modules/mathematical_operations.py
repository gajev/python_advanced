from modules_package import math_operations
initial_input = input().split()
a = float(initial_input[0])
b = float(initial_input[2])
operator = initial_input[1]

print(f'{math_operations.math_operation(a, b, operator):.2f}')
