size_matrix = int(input())

matrix = []

for _ in range(size_matrix):
    row = [int(x) for x in input().split(" ")]
    matrix.append(row)

sum_first_diagonal = 0
for number in range(size_matrix):
    sum_first_diagonal += matrix[number][number]

sum_second_diagonal = 0
for number in range(size_matrix):
    sum_second_diagonal += matrix[number][size_matrix - 1 - number]

print(abs(sum_first_diagonal - sum_second_diagonal))

