file_path = './files_for_lab/File Opener/text.txt'

try:
    file = open(file_path, 'r')
    print("File found")
except FileNotFoundError:
    print("File not found")