def get_count_letters(line):
    number_of_chars = 0
    for ch in line:
        if ch.isalpha():
            number_of_chars += 1
    return number_of_chars


def get_count_punct(line):
    counter_punct = 0
    for ch in line:
        if ch in "',.!?\";:-":
            counter_punct += 1
    return counter_punct


file_path = './text.txt'
result_path = './output.txt'

text_for_output = ""
with open(file_path, 'r') as file:
    counter_line = 1
    for line in file:
        letters = get_count_letters(line)
        punct = get_count_punct(line)
        text_for_output += f"Line: {counter_line}: {line.strip()} ({letters})({punct})\n"
        counter_line += 1

with open(result_path, 'w') as result_file:
    result_file.write(text_for_output)
