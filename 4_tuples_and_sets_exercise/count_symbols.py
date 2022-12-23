initial_word = input()
symbols_dict = {}
for symbol in initial_word:
    if symbol not in symbols_dict:
        symbols_dict[symbol] = 0
    symbols_dict[symbol] += 1
sorted_dict = sorted(symbols_dict.items())
for pair in sorted_dict:
    print(f'{pair[0]}: {pair[1]} time/s')