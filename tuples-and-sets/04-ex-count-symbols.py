text = input()

count_symbols = {}
for ch in text:
    if ch not in count_symbols:
        count_symbols[ch] = 0
    count_symbols[ch] += 1

for key, value in sorted(count_symbols.items(), key=lambda x: (x[0])):
    print(f"{key}: {value} time/s")