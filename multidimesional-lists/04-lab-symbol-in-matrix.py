def if_symbol_exists(matrix, symbol):
    for i, row in enumerate(matrix):
        for j, char in enumerate(row):
            if char == symbol:
                return i, j


n = int(input())
matrix = []

for _ in range(n):
    row = input()
    matrix.append(row)

search_symbol = input()

result = if_symbol_exists(matrix, search_symbol)

if result:
    print(result)
else:
    print(f"{search_symbol} does not occur in the matrix")