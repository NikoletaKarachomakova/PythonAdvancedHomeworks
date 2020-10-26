text_path = 'text.txt'

with open(text_path, 'r') as file:
    counter_line = 0
    for line in file:
        if counter_line % 2 == 0:
            for element in "-,.!?":
                line = line.replace(element, "@")
            words = list(reversed(line.split()))
            print(" ".join(words))
        counter_line += 1
