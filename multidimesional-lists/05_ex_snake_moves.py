from _collections import deque

rows_count, cols_count = [int(x) for x in input().split()]
text = deque(input())

matrix = [[" " for c in range(cols_count)] for r in range(rows_count)]

for row in range(rows_count):
    for col in range(cols_count):
        char = text.popleft()

        if row % 2 == 0:
            matrix[row][col] = char
        else:
            matrix[row][cols_count - 1 - col] = char
        text.append(char)

[print("".join(m)) for m in matrix]