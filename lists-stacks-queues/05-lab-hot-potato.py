from collections import deque

d = deque(input().split())
n_toss = int(input())

while len(d) > 1:
    d.rotate(-n_toss)
    print(f"Removed {d.pop()}")

print(f"Last is {d.pop()}")