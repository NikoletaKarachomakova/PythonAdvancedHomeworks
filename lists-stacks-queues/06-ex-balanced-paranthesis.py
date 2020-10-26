string = list(input())

stack = []
is_balanced = False

if string[0] == "]" or string[0] == ")" or string[0] == "}" or len(string) % 2 != 0:
    is_balanced = False
else:
    for index in range(len(string)):
        curr_symbol = string[index]
        if curr_symbol == "(" or curr_symbol == "[" or curr_symbol == "{":
            stack.append(curr_symbol)
        else:
            prev_symbol = stack[-1]
            if curr_symbol == ")" and prev_symbol == "(":
                stack.pop()
            elif curr_symbol == "]" and prev_symbol == "[":
                stack.pop()
            elif curr_symbol == "}" and prev_symbol == "{":
                stack.pop()

    if len(stack) == 0:
        is_balanced = True

if is_balanced:
    print("YES")
else:
    print("NO")
