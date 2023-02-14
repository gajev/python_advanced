from collections import deque

vowels = deque(x for x in input().split())
consonants = [x for x in input().split()]
dictionary = {"rose": "rose", "tulip": "tulip", "lotus": "lotus", "daffodil": "daffodil"}
found = False

while vowels and consonants:
    current_vowels = vowels.popleft()
    current_consonant = consonants.pop()
    for key, value in dictionary.items():
        if current_consonant in dictionary[key]:
            dictionary[key] = dictionary[key].replace(current_consonant, "")
        if current_vowels in dictionary[key]:
            dictionary[key] = dictionary[key].replace(current_vowels, "")
        if dictionary[key] == "":
            found = True
            print(f"Word found: {key}")
            break
    if found:
        break

if not found:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(x for x in vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(x for x in consonants)}")
