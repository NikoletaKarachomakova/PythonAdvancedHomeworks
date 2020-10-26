from _collections import deque
cups = deque(list(map(int, input().split(" "))))
bottles_stack = list(map(int, input().split(" ")))

wasted_water = 0
no_more_bottles = False

while len(cups) > 0:
    if len(bottles_stack) > 0:
        current_cup = cups.popleft()
        current_bottle = bottles_stack.pop()

        if current_bottle >= current_cup:
            wasted_water += current_bottle - current_cup

        else:
            current_cup -= current_bottle
            cups.appendleft(current_cup)

    else:
        no_more_bottles = True
        break

if no_more_bottles:
    print(f"Cups: {' '.join(list(map(str, cups)))}")

if len(bottles_stack) > 0:
    print(f"Bottles: {' '.join(list(map(str, bottles_stack)))}")

print(f"Wasted litters of water: {wasted_water}")


