string = input()
stack = []

for ch in string:
    stack.append(ch)

reversed_string = ""

while len(stack) > 0:
    item = stack.pop()
    reversed_string += item

print(reversed_string)