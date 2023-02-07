from collections import deque

customers = deque(int(x) for x in input().split(", "))
drivers = [int(x) for x in input().split(", ")]
total_time = 0

while customers and drivers:
    current_customer = customers.popleft()
    current_driver = drivers.pop()
    if current_driver >= current_customer:
        total_time += current_customer
    else:
        customers.insert(0, current_customer)

if not customers:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
else:
    print("Not all customers were driven to their destinations")
    print(f'Customers left: {", ".join(str(x) for x in customers)}')

