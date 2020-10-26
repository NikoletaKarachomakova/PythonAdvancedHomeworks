command = input()

numbers = list(map(int, input().split()))
length = len(numbers)
odd_sum = (sum(list(filter(lambda x: x % 2 != 0, numbers)))) * length
even_sum = (sum(list(filter(lambda x: x % 2 == 0, numbers)))) * length

if command == "Odd":
    print(f"{odd_sum}")
elif command == "Even":
    print(f"{even_sum}")