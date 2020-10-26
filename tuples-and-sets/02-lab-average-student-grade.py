n = int(input())

full_data = {}

for _ in range(n):
    command = input().split()
    name = command[0]
    grade = float(command[1])

    if name not in full_data:
        full_data[name] = []
    full_data[name].append(grade)

for student, grade in full_data.items():
    current_grades_str = " ".join(map(lambda f: format(f, '.2f'), grade))
    print(f"{student} -> {current_grades_str} (avg: {(sum(grade) / len(grade)):.2f})")