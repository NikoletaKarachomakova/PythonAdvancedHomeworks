def func_executor(*args):
    results = []

    for a in args:
        function = a[0]
        numbers_tuple = a[1]
        results.append(function(*numbers_tuple))
    return results

def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))

