# words = input().split(", ")
#
# result = [f"{w} -> {len(w)}" for w in words]
# print(", ".join(result))

words = input().split(", ")
words_with_len = {x: len(x) for x in words}
result = [f"{key} -> {value}" for key, value in words_with_len.items()]
print(", ".join(result))