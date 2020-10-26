row_count, column_count = [int(x) for x in input().split(", ")]

matrix = []
for _ in range(row_count):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)

max_sum = 0
max_submatrix = []

for i in range(row_count - 1):
    for j in range(column_count - 1):
        current_value = matrix[i][j]
        row_one = [matrix[i][j], matrix[i][j+1]]
        row_two = [matrix[i+1][j], matrix[i+1][j + 1]]
        sub_matrix = [row_one, row_two]
        sum_sub_matrix = sum(row_one) + sum(row_two)
        if sum_sub_matrix > max_sum:
            max_sum = sum_sub_matrix
            max_submatrix = sub_matrix


for row in max_submatrix:
    print(" ".join(map(str, row)))
print(max_sum)