rows, cols = [int(x) for x in input().split()]

matrix = [[f"{chr(row)}{chr(row + col)}{chr(row)}" for col in range(cols)] for row in range(97, 97 + rows)]
[print(" ".join(row)) for row in matrix]



# rows, cols = [int(x) for x in input().split()]
#
# matrix = [[[0, 0, 0] for c in range(cols)] for r in range(rows)]
#
# start_letter = 97
# new_matrix = []
#
# for row in range(rows):
#     new_row = []
#     first_last = start_letter + row
#     for col in range(cols):
#         middle = col + row + start_letter
#         current_el = matrix[row][col]
#         current_el[0] = chr(first_last)
#         current_el[2] = chr(first_last)
#         current_el[1] = chr(middle)
#         new_row.append("".join(current_el))
#     new_matrix.append(new_row)
#
# for x in new_matrix:
#     print(" ".join(x))