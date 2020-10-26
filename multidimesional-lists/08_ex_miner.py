import itertools

n = int(input())
commands = input().split()
matrix = [input().split() for _ in range(n)]

initial_pos_miner = []
for r in range(n):
    for c in range(n):
        if matrix[r][c] == "s":
            initial_pos_miner = [r, c]
            break

matrix_to_list = list(itertools.chain(*matrix))
total_coal = matrix_to_list.count("c")
coal_collected = 0
current_position = initial_pos_miner
current_row, current_col = current_position[0], current_position[1]
is_game_finished = False

for command in commands:
    if command == "left":
        step_col = current_col - 1
        if 0 <= step_col < n:
            current_position = [current_row, step_col]

    elif command == "right":
        step_col = current_col + 1
        if 0 <= step_col < n:
            current_position = [current_row, step_col]

    elif command == "up":
        step_row = current_row - 1
        if 0 <= step_row < n:
            current_position = [step_row, current_col]

    elif command == "down":
        step_row = current_row + 1
        if 0 <= step_row < n:
            current_position = [step_row, current_col]

    current_row = current_position[0]
    current_col = current_position[1]

    if matrix[current_row][current_col] == "e":
        print(f"Game over! ({current_row}, {current_col})")
        is_game_finished = True
        break

    elif matrix[current_row][current_col] == "c":
        coal_collected += 1
        matrix[current_row][current_col] = "*"
        if coal_collected == total_coal:
            print(f"You collected all coals! ({current_row}, {current_col})")
            is_game_finished = True
            break

if not is_game_finished:
    print(f"{total_coal - coal_collected} coals left. ({current_position[0]}, {current_position[1]})")