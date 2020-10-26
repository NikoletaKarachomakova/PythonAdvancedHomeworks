import itertools
line = input()

result = [item.split() for item in line.split("|")[::-1]]
print(" ".join(itertools.chain(*result)))