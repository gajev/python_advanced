from math import log

number = int(input())
logarithm_base = input()
if logarithm_base == "natural":
    print(f"{log(number):.2f}")
else:
    try:
        print(f"{log(number, int(logarithm_base)):.2f}")
    except:
        raise ValueError
