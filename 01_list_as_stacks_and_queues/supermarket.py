from collections import deque
q = deque()
command = input()
while command != "End":
    if command == "Paid":
        print("\n".join(q))
        q = deque()
    else:
        q.append(command)
    command = input()
print(f'{len(q)} people remaining.')

