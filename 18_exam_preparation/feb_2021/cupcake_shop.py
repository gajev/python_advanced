def stock_availability(initial_list, delivery_or_sell, *args):
    if delivery_or_sell == "delivery":
        for item in args:
            initial_list.append(item)
    elif delivery_or_sell == "sell":
        if not args:
            initial_list.pop(0)
        else:
            for item in args:
                if type(item) == int:
                    for current_item in range(item):
                        initial_list.pop(0)
                else:
                    if item in initial_list:
                        initial_list = [x for x in initial_list if x != item]
    return initial_list


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))




