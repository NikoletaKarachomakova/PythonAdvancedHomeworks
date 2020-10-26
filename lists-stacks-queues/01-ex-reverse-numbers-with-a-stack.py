numbers = list(map(int, input().split()))

reversed = []
while len(numbers) > 0:
    reversed.append(str(numbers.pop()))

print(" ".join(reversed))