file_path = './files_for_lab/File Reader/numbers.txt'

numbers_str = open(file_path, 'r')
sum  = 0
for line in numbers_str:
    number = int(line)
    sum += number

print(sum)

# numbers_str = open(file_path, 'r')
# sum  = 0
# while True:
#     n = numbers_str.readline()
#     if not n:
#         break
#     sum += int(n)
#
# print(sum)