from collections import deque

price_bullet = int(input())
gun_barrels = int(input())
bullets = list(map(int, input().split(" ")))
locks = deque(list(map(int, input().split(" "))))
value = int(input())

total_shot = 0
run_out_of_bullets = False
available_per_barrel = gun_barrels

while len(locks) > 0:
    if len(bullets) > 0:
        current_lock = locks.popleft()
        current_bullet = bullets.pop()
        available_per_barrel -= 1
        total_shot += 1
        if current_bullet > current_lock:
            locks.appendleft(current_lock)
            print("Ping!")
        else:
            print("Bang!")

        if available_per_barrel == 0 and len(bullets) >= 1:
            print("Reloading!")
            available_per_barrel = gun_barrels
    else:
        run_out_of_bullets = True
        break

if run_out_of_bullets:
    print(f"Couldn't get through. Locks left: {len(locks)}")

earned_money = value - (total_shot * price_bullet)
if len(locks) == 0:
    print(f"{len(bullets)} bullets left. Earned ${earned_money}")