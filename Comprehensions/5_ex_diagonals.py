rows_count = int(input())

matrix = [[int(x) for x in input().split(", ")] for _ in range(rows_count)]

first_diagonal = [matrix[row][row] for row in range(rows_count)]

second_diagonal = [matrix[x][rows_count -1 - x] for x in range(rows_count)]

print(f"First diagonal: {', '.join(list(map(str, first_diagonal)))}. Sum: {sum(first_diagonal)}")
print(f"Second diagonal: {', '.join(list(map(str, second_diagonal)))}. Sum: {sum(second_diagonal)}")