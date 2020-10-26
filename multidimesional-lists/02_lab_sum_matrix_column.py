row, column = list(map(int, input().split(", ")))

matrix = []


for r in range(row):
    current_row = [int(n) for n in input().split(" ")]
    matrix.append(current_row)

for j in range(column):
    total = 0
    for r in matrix:
        total += r[j]
    print(total)
