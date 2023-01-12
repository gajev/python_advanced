from collections import deque
food_quantity = int(input())
orders = deque(map(int, input().split()))
print(max(orders))
for current_order in range(len(orders)):
    if food_quantity >= orders[0]:
        food_quantity -= orders.popleft()
    else:
        break
if orders:
    orders_string = ''
    for _ in range(len(orders)):
        orders_string += str(orders.popleft()) + " "
    print(f"Orders left: {orders_string}")
else:
    print("Orders complete")
