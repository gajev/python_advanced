def forecast(*args):
    weather_dict = {}
    for current_tuple in args:
        if current_tuple[1] not in weather_dict:
            weather_dict[current_tuple[1]] = []
        weather_dict[current_tuple[1]].append(current_tuple[0])
    for key, value in weather_dict.items():
        weather_dict[key] = sorted(value)
    result = ""
    if "Sunny" in weather_dict.keys():
        for city in weather_dict["Sunny"]:
            result += f"{city} - Sunny\n"
    if "Cloudy" in weather_dict.keys():
        for city in weather_dict["Cloudy"]:
            result += f"{city} - Cloudy\n"
    if "Rainy" in weather_dict.keys():
        for city in weather_dict["Rainy"]:
            result += f"{city} - Rainy\n"
    return result


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))