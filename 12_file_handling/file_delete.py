import os

try:
    os.remove("file_does_not_exist.txt")
except FileNotFoundError:
    print("File already deleted!")
