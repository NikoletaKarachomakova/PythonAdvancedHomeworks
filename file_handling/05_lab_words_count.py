words_file = './files_for_lab/Words Count/words.txt'
text_file = './files_for_lab/Words Count/text.txt'

word_search = []
with open(words_file, 'r') as file_w:
    word_search = file_w.read().split()

words_count = {word: 0 for word in word_search}

with open(text_file, 'r') as file_t:
    for line in file_t:
        for word in word_search:
            if word in line.lower():
                words_count[word] += 1
print(words_count)

sort_dict = dict(sorted(words_count.items(), key=lambda x: -x[1]))

for key, value in sort_dict.items():
    print(f"{key}-{value}")

