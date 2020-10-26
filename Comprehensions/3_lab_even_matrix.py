rows_counter = int(input())

matrix = []
for _ in range(rows_counter):
    row = list(map(int, input().split(", ")))
    matrix.append(row)

even_matrix = [[x for x in row if x % 2 == 0] for row in matrix]
print(even_matrix)