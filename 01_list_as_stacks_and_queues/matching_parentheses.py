initial_input = input()
temp_list = []
for index, current_element in enumerate(initial_input):
    if current_element == "(":
        temp_list.append(index)
    elif current_element == ")":
        print(initial_input[temp_list[-1]:index + 1])
        temp_list.pop()
