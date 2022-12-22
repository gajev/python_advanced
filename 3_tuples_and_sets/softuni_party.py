number_of_people = int(input())
set_people = set()
for _ in range(number_of_people):
    guest = input()
    set_people.add(guest)
command = input()
while command != "END":
    if command in set_people:
        set_people.remove(command)
    command = input()
print(len(set_people))
for missing_guest in sorted(set_people):
    print(missing_guest)

