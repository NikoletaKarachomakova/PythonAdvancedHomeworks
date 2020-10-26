input_n = list(map(int, input().split()))
sum_n = sum(input_n)

set_first = set()
set_second = set()

for n in range(sum_n):
    number = int(input())
    if 0 <= n < (sum_n - input_n[1]):
        set_first.add(number)
    else:
        set_second.add(number)

unique_elem = set_second & set_first
print("\n".join(list(map(str, unique_elem))))

