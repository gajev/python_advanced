def naughty_or_nice_list(santa_list, *args, **kwargs):
    nice_kids = []
    naughty_kids = []
    not_found = []
    numbers_dict = {}
    names_dict = {}

    for element in args:
        number = int(element.split("-")[0])
        type_of_kid = element.split("-")[1]
        counter = 0
        name = ""
        index_santa = 0
        for index in range(len(santa_list)):
            if number == santa_list[index][0]:
                counter += 1
                name = santa_list[index][1]
                index_santa = index

        if counter == 1:
            santa_list.pop(index_santa)
            if type_of_kid == "Nice":
                nice_kids.append(name)
            else:
                naughty_kids.append(name)

    for key, value in kwargs.items():
        counter_ = 0
        kid_name = ""
        index_santa = 0
        for index_ in range(len(santa_list)):
            if key == santa_list[index_][1]:
                counter_ += 1
                index_santa = index_
                kid_name = key
        if counter_ == 1:
            santa_list.pop(index_santa)
            if kwargs[key] == "Nice":
                nice_kids.append(kid_name)
            else:
                naughty_kids.append(kid_name)
    for kid in santa_list:
        not_found.append(kid[1])
    result = ""
    if nice_kids:
        result += f"Nice: {', '.join(x for x in nice_kids)}\n"
    if naughty_kids:
        result += f"Naughty: {', '.join(x for x in naughty_kids)}\n"
    if not_found:
        result += f"Not found: {', '.join(x for x in not_found)}"

    return result

print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))