import os

path = input()
sep_count = path.count(os.path.sep)
results = {}

for root, dirs, files in os.walk(path):
    if root.count(os.path.sep) - sep_count > 1:
        continue
    for file in files:
        extension = file.split(".")[-1]
        if extension not in results:
            results[extension] = []
        results[extension].append(file)

report = ""
for key, value in sorted(results.items()):
    report += f".{key}\n"
    for v in sorted(value):
        report += f"- - - {v}\n"

desktop_loc = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
final_loc = desktop_loc + os.path.sep + 'report.txt'

with open(final_loc, 'w') as file:
    file.write(report)
