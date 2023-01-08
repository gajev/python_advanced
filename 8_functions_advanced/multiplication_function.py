def multiply(*args):
    result = 1
    for element in args:
        result *= element
    return result
print(multiply(1, 4, 5))