n = int(input())

matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split()])

coordinates = [x.split(",") for x in input().split()]

for coord in coordinates:
    bomb_row = int(coord[0])
    bomb_col = int(coord[1])
    value_bomb = matrix[bomb_row][bomb_col]

    rows_range = [-1, -1, -1, 0, 0, 1, 1, 1]
    columns_range = [-1, 0, 1, -1, 1, -1, 0, 1]

    for i in range(8):
        possible_hit_row = rows_range[i]
        possible_hit_col = columns_range[i]
        r = bomb_row + possible_hit_row
        c = bomb_col + possible_hit_col

        if 0 <= r < n and 0 <= c < n and matrix[r][c] > 0 and value_bomb > 0:
            matrix[r][c] -= value_bomb
        if value_bomb > 0:
            matrix[bomb_row][bomb_col] = 0

alive_cells = 0
sum_alive = 0
for row in matrix:
    for x in row:
        if x > 0:
            alive_cells += 1
            sum_alive += x

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_alive}")
[print(" ".join(list(map(str, r)))) for r in matrix]
