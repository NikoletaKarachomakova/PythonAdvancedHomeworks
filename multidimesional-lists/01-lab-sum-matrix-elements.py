row, column = list(map(int, input().split(", ")))

matrix = []
total = 0

for r in range(row):
    current_row = list(map(int, input().split(", ")))
    # curent_row = [int(number) for number in input().split(", ")]
    matrix.append(current_row)
    total += sum(current_row)

print(total)
print(matrix)