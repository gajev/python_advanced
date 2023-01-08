def rectangle(length, width):
    def area():
        area_result = f"Rectangle area: {length * width}"
        return area_result


    def perimeter():
        perimeter_result = f"Rectangle perimeter: {2 * length + 2 * width}"
        return perimeter_result

    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"
    return area() + "\n" + perimeter()
print(rectangle(5, 10))