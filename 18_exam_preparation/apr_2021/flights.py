def flights(*args):
    flight_dict = {}
    temp_city = ""
    for element in args:
        if element == "Finish":
            break
        else:
            if type(element) == int:
                flight_dict[temp_city] += element
            else:
                temp_city = element
                if temp_city not in flight_dict:
                    flight_dict[temp_city] = 0
    return flight_dict


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))