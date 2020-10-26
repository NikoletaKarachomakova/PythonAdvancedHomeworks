phone_book = {}

num_names = 0

while True:
    next_input = input()

    if next_input.isdigit():
        num_names = int(next_input)
        break

    else:
        name, phone = next_input.split("-")
        phone_book[name]  = phone


for _ in range(num_names):
    name = input()
    if name in phone_book.keys():
        print(f"{name} -> {phone_book[name]}")
    else:
        print(f"Contact {name} does not exist.")