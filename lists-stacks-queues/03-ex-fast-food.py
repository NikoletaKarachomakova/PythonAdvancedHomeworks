from _collections import deque

quantity_food = int(input())

orders = deque(map(int, input().split()))
print(max(orders))

while len(orders) > 0:
    if quantity_food >= orders[0]:
        quantity_food -= orders.popleft()
    else:
        break

if len(orders) == 0:
    print("Orders complete")
else:
    orders_to_string = list(map(str, orders))
    print(f"Orders left: {' '.join(orders_to_string)}")