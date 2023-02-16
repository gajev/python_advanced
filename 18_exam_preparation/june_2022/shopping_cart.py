def shopping_cart(*args):
    dictionary = {"Soup": [], "Pizza": [], "Dessert": []}
    list_empty = 0
    for element in args:
        if element == "Stop":
            break
        type_meal = element[0]
        product = element[1]
        if type_meal == "Soup" and len(dictionary[type_meal]) < 3:
            if product not in dictionary[type_meal]:
                dictionary[type_meal].append(product)
                list_empty += 1
        elif type_meal == "Pizza" and len(dictionary[type_meal]) < 4:
            if product not in dictionary[type_meal]:
                dictionary[type_meal].append(product)
                list_empty += 1
        elif type_meal == "Dessert" and len(dictionary[type_meal]) < 2:
            if product not in dictionary[type_meal]:
                dictionary[type_meal].append(product)
                list_empty += 1

    for k, v in dictionary.items():
        dictionary[k] = sorted(dictionary[k])

    dictionary = sorted(dictionary.items(), key=lambda x: (-len(x[1]), x))
    result = ""
    if list_empty > 0:
        for el in dictionary:
            result += f"{el[0]}:\n"
            for element in el[1]:
                result += f" - {element}\n"
    else:
        return "No products in the cart!"

    return result


print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))