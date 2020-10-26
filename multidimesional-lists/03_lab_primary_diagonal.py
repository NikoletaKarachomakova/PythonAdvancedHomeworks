n = int(input())

matrix = []
total = 0
for _ in range(n):
    row = list(map(int, input().split(" ")))
    matrix.append(row)

for x in range(len(matrix)):
    value = matrix[x][x]
    total += value

print(total)