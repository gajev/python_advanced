import re

words_dictionary = {}
with open("words.txt", "r") as words_file:
    all_words = words_file.read().split()
    for word in all_words:
        words_dictionary[word.lower()] = 0

with open("input.txt", "r") as text_file:
    for line in text_file:
        all_line_words = re.findall("[A-z\']+", line)
        for current_word in all_line_words:
            current_word_lower = current_word.lower()
            if current_word_lower in words_dictionary:
                words_dictionary[current_word_lower] += 1
sorted_dict = sorted(words_dictionary.items(), key=lambda x: -x[1])
for item in sorted_dict:
    print(f'{item[0]} - {item[1]}')