rows, cols = (int(x) for x in input().split())
word = input()
index = 0
for i in range(rows):
    current_word = []
    for j in range(cols):
        current_word.append(word[index % len(word)])
        index += 1
    if i % 2 == 0:
        print("".join(current_word))
    else:
        print("".join(reversed(current_word)))

