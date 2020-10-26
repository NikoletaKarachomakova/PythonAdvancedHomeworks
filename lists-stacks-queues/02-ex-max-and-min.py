counter = int(input())

stack = []

for _ in range(counter):
    current_row = list(map(int, input().split()))
    operation = current_row[0]

    if operation == 1:
        number = current_row[1]
        stack.append(number)

    if len(stack) > 0:
        if operation == 2:
            stack.pop()

        elif operation == 3:
            print(max(stack))

        elif operation == 4:
            print(min(stack))

reversed_stack = []
while len(stack) > 0:
    reversed_stack.append(str(stack.pop()))

print(", ".join(reversed_stack))
