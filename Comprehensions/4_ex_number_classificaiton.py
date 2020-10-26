numbers = list(map(int, input().split(", ")))

positive_num = [str(num) for num in numbers if num >= 0]
negative_num = [str(num) for num in numbers if num < 0]
even_num = [str(num) for num in numbers if num % 2 == 0]
odd_num = [str(num) for num in numbers if num % 2 != 0]

print(f'Positive: {", ".join(positive_num)}')
print(f'Negative: {", ".join(negative_num)}')
print(f'Even: {", ".join(even_num)}')
print(f'Odd: {", ".join(odd_num)}')