def math_operation(a, b, operator):
    result = 0
    if operator == "+":
        result = a + b

    elif operator == "-":
        result = a - b

    elif operator == "/":
        result = a / b

    elif operator == "*":
        result = a * b

    elif operator == "^":
        result = a ** b

    return result
