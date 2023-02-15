def add_songs(*args):
    dictionary = {}
    for current_tuple in args:
        if current_tuple[0] not in dictionary:
            dictionary[current_tuple[0]] = current_tuple[1]
        else:
            dictionary[current_tuple[0]].extend(current_tuple[1])
    result = ""
    for key, value in dictionary.items():
        result += f"- {key}\n"
        for v in value:
            result += f"{v}\n"
    return result


print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))