number_of_names = int(input())
set_names = set()
for student in range(number_of_names):
    set_names.add(input())
for name in set_names:
    print(name)