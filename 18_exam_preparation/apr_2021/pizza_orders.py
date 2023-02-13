from collections import deque

pizza_orders = deque(int(x) for x in input().split(", "))
employee_capacity = [int(x) for x in input().split(", ")]
total_pizzas = 0

while pizza_orders and employee_capacity:
    current_pizza = pizza_orders.popleft()
    current_employee = employee_capacity.pop()
    if not 0 < current_pizza <= 10:
        employee_capacity.append(current_employee)
        continue
    if current_employee >= current_pizza:
        total_pizzas += current_pizza
    else:
        remaining_pizzas = current_pizza - current_employee
        pizza_orders.appendleft(remaining_pizzas)
        total_pizzas += current_employee

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    print(f"Employees: {', '.join(str(x)for x in employee_capacity)}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x)for x in pizza_orders)}")


