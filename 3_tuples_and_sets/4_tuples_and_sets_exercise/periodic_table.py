number = int(input())
elements = set()
for _ in range(number):
    current_elements = input().split()
    for element in current_elements:
        elements.add(element)
for current_element in elements:
    print(current_element)