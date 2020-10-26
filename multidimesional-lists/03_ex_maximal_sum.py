row_count, column_count = [int(x) for x in input().split()]

matrix = []
for _ in range(row_count):
    line = [int(x) for x in input().split()]
    matrix.append(line)

winning_matrix = []
max_value = -9999999999

for i in range(row_count - 2):
    for j in range(column_count - 2):
        sub_matrix = []
        sum_sub_matrix = 0

        for counter_row in range(i, i+3):
            current_row = []
            for counter_column in range(j, j+3):
                value = matrix[counter_row][counter_column]
                current_row.append(value)
            sub_matrix.append(current_row)

        for mtx in sub_matrix:
            sum_sub_matrix += sum(mtx)
        if sum_sub_matrix > max_value:
            max_value = sum_sub_matrix
            winning_matrix = sub_matrix

print(f"Sum = {max_value}")
for row in winning_matrix:
    print(" ".join(map(str, row)))
