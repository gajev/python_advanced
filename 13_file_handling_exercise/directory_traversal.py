# Use ./directory_traversal as input

import os


directory = input()
extensions = {}
for filename in os.listdir(directory):

    file = os.path.join(directory, filename)

    if os.path.isfile(file):
        extension = filename.split(".")[1]
        if extension not in extensions:
            extensions[extension] = []
        extensions[extension].append(filename)

sorted_extensions = sorted(extensions.items(), key=lambda x: (x[0], x[1]))
report = open(f"./{directory}/report.txt", "a")
for current_extension in sorted_extensions:
    report.write(f"{current_extension[0]}\n")
    for current_file in current_extension[1]:
        report.write(f'- - - {current_file}\n')
report.close()

