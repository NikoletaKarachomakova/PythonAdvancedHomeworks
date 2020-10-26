rows_count = int(input())

matrix = []
for row in range(rows_count):
    current_row = list(map(int, input().split(", ")))
    matrix.append(current_row)

flattened_matrix = [symbol for item in matrix for symbol in item]

print(flattened_matrix)