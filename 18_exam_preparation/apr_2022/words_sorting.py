def words_sorting(*args):
    dictionary = {}
    total = 0
    for item in args:
        value = 0
        for character in item:
            value += ord(character)
        dictionary[item] = value
        total += value

    if total % 2 == 0:
        sorted_dict = sorted(dictionary.items(), key=lambda x: (x[0]))
    else:
        sorted_dict = sorted(dictionary.items(), key=lambda x: (-x[1]))
    result = f""
    for k, v in sorted_dict:
        result += f"{k} - {v}\n"
    return result


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))