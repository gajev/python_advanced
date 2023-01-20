symbols = ["-", ",", ".", "!", "?"]

with open("files/text.txt") as even_lines_file:

    text = even_lines_file.readlines()

    for current_row in range(0, len(text), 2):
        for current_symbol in symbols:
            text[current_row] = text[current_row].replace(current_symbol, "@")

        print(*text[current_row].split()[::-1], sep=" ")
        print("")










