from collections import deque

bowls = [int(x) for x in input().split(", ")]
customers = deque(int(x) for x in input().split(", "))

while bowls and customers:
    current_ramen = bowls.pop()
    current_customer = customers.popleft()
    if current_customer == current_ramen:
        pass
    elif current_ramen > current_customer:
        difference = current_ramen - current_customer
        bowls.append(difference)
    else:
        difference = current_customer - current_ramen
        customers.appendleft(difference)

if customers:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")
else:
    print("Great job! You served all the customers.")
    if bowls:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls)}")

