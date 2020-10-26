def concatenate(*args):
    concat_str = ""
    for a in args:
        concat_str += a
    return concat_str

print(concatenate("Soft", "Uni", "Is", "Great", "!"))