n, m = map(int, input().split())
first_set = set()
second_set = set()
for number_n in range(n):
    first_set.add(int(input()))
for number_m in range(m):
    second_set.add(int(input()))
result = first_set.intersection(second_set)
for number in result:
    print(number)