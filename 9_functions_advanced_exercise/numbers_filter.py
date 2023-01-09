def even_odd_filter(**kwargs):
    final_dict = {}
    for key, value in kwargs.items():
        parity = 0 if key == "even" else 1
        filtered = [x for x in value if x % 2 == parity]
        final_dict[key] = filtered
    return dict(sorted(final_dict.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
