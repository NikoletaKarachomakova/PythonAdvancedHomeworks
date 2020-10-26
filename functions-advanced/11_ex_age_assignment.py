def age_assignment(*args, **kwargs):
    names = args
    ages = kwargs
    dict_results = {}

    for name in names:
        first_letter = name[0]
        for key, value in ages.items():
            if first_letter == key:
                dict_results[name] = value
                break

    return dict_results


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))