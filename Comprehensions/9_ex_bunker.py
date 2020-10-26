bunker = {i: {} for i in input().split(", ")}
n = int(input())

for _ in range(n):
    tokens = input().split(" - ")
    category = tokens[0]
    item = tokens[1]
    qnt_qlt = tokens[2].split(";")
    quantity = int(qnt_qlt[0].split(":")[1])
    quality = int(qnt_qlt[1].split(":")[1])

    bunker[category][item] = (quantity, quality)

all_quantities = [list(bunker[category].values()) for category in bunker]
sum_qnt = 0
sum_qlt = 0
for x in all_quantities:
  for y in x:
    sum_qnt += y[0]
    sum_qlt += y[1]

print(f"Count of items: {sum_qnt}")
print(f" Average quality: {(sum_qlt / len(bunker)):.2f}")

for cat in bunker:
  items = [i  for i in bunker[cat].keys()]
  print(f"{cat} -> {', '.join(items)}")