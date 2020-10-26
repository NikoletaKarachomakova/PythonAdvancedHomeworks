symbols = input().split(", ")

ascii_values = {symbol: ord(symbol) for symbol in symbols}
print(ascii_values)