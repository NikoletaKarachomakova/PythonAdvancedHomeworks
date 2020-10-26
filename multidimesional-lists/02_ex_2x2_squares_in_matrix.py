row_count, column_count = [int(x) for x in input().split(" ")]

matrix = []
for _ in range(row_count):
    row = input().split(" ")
    matrix.append(row)

equal_chars = 0

for i in range(row_count - 1):
    for j in range(column_count - 1):
        current_ch = matrix[i][j]
        if current_ch == matrix[i][j+1] == matrix[i+1][j] == matrix[i+1][j+1]:
            equal_chars += 1

print(equal_chars)
