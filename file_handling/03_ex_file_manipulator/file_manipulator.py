import os

command = input()
while command != "End":
    tokens = command.split("-")
    act = tokens[0]
    file_name = tokens[1]

    if act == "Create":
       with open(file_name, 'w') as file:
            file.write("")

    elif act == "Add":
        content = tokens[2]
        with open(file_name, 'a') as file:
            file.write( f"{content}\n")

    elif act == "Replace":
        old_string = tokens[2]
        new_string = tokens[3]
        if os.path.exists(file_name):
            text = ""
            with open(file_name, 'r') as file:
                text = file.read()
            text = text.replace(old_string, new_string)
            with open(file_name, 'w') as file:
                file.write(text)
        else:
            print("An error occurred")

    elif act == "Delete":
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")

    command = input()
