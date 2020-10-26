rows = int(input())

set_odd = set()
set_even = set()

for row in range(1, rows + 1):
    ascii_value_name = sum(map(ord, input()))
    divide_by_row = ascii_value_name // row

    if divide_by_row % 2 == 0:
        set_even.add(divide_by_row)
    else:
        set_odd.add(divide_by_row)

sum_odd = sum(set_odd)
sum_even = sum(set_even)

value = set()

if sum_odd == sum_even:
    value = set_odd | set_even
elif sum_odd > sum_even:
    value = set_odd - set_even
else:
    value = set_odd ^ set_even

print(", ".join(list(map(str, value))))