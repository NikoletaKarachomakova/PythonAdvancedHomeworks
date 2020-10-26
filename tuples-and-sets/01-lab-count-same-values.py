numbers = list(map(float, input().split()))

dict_numbers = {}

for n in numbers:
    if n not in dict_numbers:
        dict_numbers[n] = 0
    dict_numbers[n] += 1

for number, counter in dict_numbers.items():
    print(f"{number} - {counter} times")