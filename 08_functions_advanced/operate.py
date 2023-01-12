def operate(operator, *args):
    def sum_elements():
        return sum(args)

    def subtract():
        result = 0
        for index, element in enumerate(args):
            if index == 0:
                result = element
            else:
                result -= element
        return result

    def multiply():
        result = 1
        for element in args:
            result *= element
        return result

    def divide():
        result = 0
        for index, element in enumerate(args):
            if index == 0:
                result = element
            else:
                if element != 0:
                    result /= element
        return result

    if operator == "+":
        return sum_elements()
    elif operator == "-":
        return subtract()
    elif operator == "*":
        return multiply()
    elif operator == "/":
        return divide()


print(operate("/", 2, 2, 0))
