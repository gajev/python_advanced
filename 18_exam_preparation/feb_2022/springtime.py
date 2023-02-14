def start_spring(**kwargs):
    reversed_dict = {}
    for key, value in kwargs.items():
        if value not in reversed_dict:
            reversed_dict[value] = []
            reversed_dict[value].append(key)
        else:
            reversed_dict[value].append(key)

    for k, v in reversed_dict.items():
        reversed_dict[k] = sorted(reversed_dict[k])

    sorted_dict = sorted(reversed_dict.items(), key=lambda x: (-len(x[1]), x))
    result = ""
    for el in sorted_dict:
        result += f"{el[0]}:\n"
        for element in el[1]:
            result += f"-{element}\n"

    return result


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
