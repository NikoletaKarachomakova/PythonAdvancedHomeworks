start_number = int(input())
end_number = int(input())


def is_number_valid(number):
    return len([True for d in range(2, 11) if number % d == 0]) > 0


numbers = [num for num in range(start_number, end_number +1) if is_number_valid(num)]

print(numbers)