number_of_names = int(input())
even_set = set()
odd_set = set()
for _ in range(1, number_of_names + 1):
    name = input()
    ascii_sum = 0
    for current_symbol in name:
        ascii_sum += ord(current_symbol)
    ascii_sum //= _
    if ascii_sum % 2 == 0:
        even_set.add(ascii_sum)
    else:
        odd_set.add(ascii_sum)
sum_even = sum(even_set)
sum_odd = sum(odd_set)
if sum_odd == sum_even:
    result = odd_set.union(even_set)
elif sum_odd > sum_even:
    result = odd_set.difference(even_set)
else:
    result = odd_set.symmetric_difference(even_set)
print(*result, sep=", ")

