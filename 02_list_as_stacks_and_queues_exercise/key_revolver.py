from collections import deque

price_of_bullet = int(input())
size_of_barrel = int(input())
bullets = [int(x) for x in input().split()]
locks = deque(int(x) for x in input().split())
intelligence_value = int(input())
money_spent = 0
counter = 0
for bullet in reversed(bullets):
    money_spent += price_of_bullet
    counter += 1
    if bullet <= locks[0]:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")
    bullets.pop()
    if counter == size_of_barrel and bullets:
        print("Reloading!")
        counter = 0
    if not locks:
        price = intelligence_value - money_spent
        print(f'{len(bullets)} bullets left. Earned ${price}')
        quit()
print(f"Couldn't get through. Locks left: {len(locks)}")
