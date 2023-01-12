initial_string = input()
brackets = []
brackets_dict = {"(": ")", "{": "}", "[": "]"}
balanced = True
for element in initial_string:
    if element in "({[":
        brackets.append(element)
    elif not brackets:
        balanced = False
        break
    else:
        if element == brackets_dict[brackets[-1]]:
            brackets.pop()
        else:
            balanced = False
            break
if not balanced or brackets:
    print("NO")
else:
    print("YES")
