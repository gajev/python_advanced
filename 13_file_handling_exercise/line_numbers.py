from string import punctuation

output_file = open("files/output.txt", "a")

with open("files/text.txt", "r") as text_file:

    text = text_file.readlines()

    for index in range(len(text)):
        letters = 0
        punctuation_marks = 0

        for symbol in text[index]:
            if symbol.isalpha():
                letters += 1
            elif symbol in punctuation:
                punctuation_marks += 1

        output_file.write(f'Line {index + 1}: {"".join(text[index][:-1])} ({letters})({punctuation_marks})\n')

output_file.close()
