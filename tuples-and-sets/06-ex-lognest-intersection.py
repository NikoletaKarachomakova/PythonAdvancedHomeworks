rows = int(input())

intersections = []

for _ in range(rows):
    first_row_range, second_row_range = tuple(input().split("-"))

    first_row_starting, first_row_ending = tuple(first_row_range.split(","))
    first_row_numbers = set(range(int(first_row_starting), int(first_row_ending) + 1))

    second_row_starting, second_row_ending = tuple(second_row_range.split(","))
    second_row_numbers = set(range(int(second_row_starting), int(second_row_ending) + 1))

    current_intersection = first_row_numbers & second_row_numbers
    intersections.append(current_intersection)

biggest_len = 0
spec_set = []

for i in intersections:
    current_len = len(i)
    if current_len >= biggest_len:
        biggest_len = current_len
        spec_set = list(i)

print(f"Longest intersection is {spec_set} with length {biggest_len}")