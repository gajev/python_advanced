import os

while True:
    command = input().split("-")
    if command[0] == "End":
        break

    elif command[0] == "Create":
        file_created = open(f"files/{command[1]}", "w")
        file_created.close()

    elif command[0] == "Add":
        with open(f"files/{command[1]}", "a") as text_file:
            text_file.write(f"{command[2]}\n")

    elif command[0] == "Replace":
        try:
            with open(f"files/{command[1]}", "r+") as file:
                file_content = file.read().replace(command[2], command[3])
                file.seek(0)
                file.truncate()
                file.write(file_content)
        except FileNotFoundError:
            print("An error occurred")

    elif command[0] == "Delete":
        try:
            os.remove(f"files/{command[1]}")
        except FileNotFoundError:
            print("An error occurred")
