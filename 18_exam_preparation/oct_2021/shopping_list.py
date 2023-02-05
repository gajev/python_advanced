def shopping_list(money, **kwargs):
    result = []
    products = 0
    if money < 100:
        return "You do not have enough budget."
    for product, value in kwargs.items():
        quantity, price = value
        total_price = quantity * price
        if money >= total_price:
            result.append(f"You bought {product} for {total_price:.2f} leva.")
            money -= total_price
            products += 1
        if products == 5:
            break
    return "\n".join(result)


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
