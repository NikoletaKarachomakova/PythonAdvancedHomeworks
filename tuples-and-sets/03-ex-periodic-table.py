number = int(input())

all_elem = set()

for n in range(number):
    elements = input().split()
    for e in elements:
        all_elem.add(e)

for e in all_elem:
    print(e)