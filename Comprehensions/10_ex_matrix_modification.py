size = int(input())

matrix =[[int(x) for x in input().split()] for _ in range(size)]

while True:
  line = input()
  if line == "END":
    break
  tokens = line.split()
  row = int(tokens[1])
  col = int(tokens[2])
  value = int(tokens[3])

  if 0 <= row < size and 0 <= col < size:
    if tokens[0] == "Add":
      matrix[row][col] += value
    elif tokens[0] == "Subtract":
      matrix[row][col] -= value

  else:
    print("Invalid coordinates")


for i in matrix:
  print(" ".join([str(x) for x in i]))