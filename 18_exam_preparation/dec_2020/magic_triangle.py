def get_magic_triangle(n):
    output_list = []
    for i in range(1, n + 1):
        temp_list = []
        for k in range(i):
            temp_list.append(1)
        output_list.append(temp_list)
    for index in range(2, n):
        for element_index in range(len(output_list[index]) + 1):
            if element_index == 0:
                continue
            try:
                output_list[index][element_index] = output_list[index - 1][element_index] \
                                                    + output_list[index - 1][element_index - 1]
            except IndexError:
                pass

    return output_list


print(get_magic_triangle(5))
