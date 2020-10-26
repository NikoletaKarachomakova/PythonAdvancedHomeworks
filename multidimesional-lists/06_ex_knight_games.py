def get_killed_knights(row, col, n, board):
    rows = [-2, -1, 1, 2, -2, -1, 1, 2]
    cols = [-1, -2, -2, -1, 1, 2, 2, 1]
    killed = 0
    for i in range(8):
        r = rows[i]
        c = cols[i]
        if 0 <= row + r < n and 0 <= col + c < n and board[row + r][col + c] == "K":
            killed += 1
    return killed


n = int(input())

board = []
for _ in range(n):
    board.append([x for x in input()])

total_kill = 0

while True:
    most_killed = 0
    to_kill = []
    for row in range(n):
        for col in range(n):
            if board[row][col] == "K":
                killed_knights = get_killed_knights(row, col, n, board)
                if killed_knights > most_killed:
                    most_killed = killed_knights
                    to_kill = [row, col]

    if most_killed == 0:
        break

    board[to_kill[0]][to_kill[1]] = "0"
    total_kill += 1

print(total_kill)