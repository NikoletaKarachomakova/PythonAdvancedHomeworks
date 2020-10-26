from _collections import deque

queue = deque()
string = input()

while string != "End":
    if string != "Paid":
        queue.append(string)

    elif string == "Paid":
        while len(queue) > 0:
            print(queue.popleft())

    string = input()

print(f"{len(queue)} people remaining.")