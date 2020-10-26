row_count, column_count = [int(x) for x in input().split()]

matrix = []
for _ in range(row_count):
    line = [x for x in input().split()]
    matrix.append(line)

command = input()
while command != "END":
    tokens = command.split()
    if len(tokens) != 5:
        print("Invalid input!")
    else:
        word = tokens[0]
        row1 = int(tokens[1])
        col1 = int(tokens[2])
        row2 = int(tokens[3])
        col2 = int(tokens[4])

        if word != "swap":
            print("Invalid input!")
        elif row1 not in range(0, row_count) or row2 not in range(0, row_count):
            print("Invalid input!")
        elif col1 not in range(0, column_count) or col2 not in range(0, column_count):
            print("Invalid input!")
        else:
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            for row in matrix:
                print(" ".join(map(str, row)))

    command = input()
