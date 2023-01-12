def age_assignment(*args, **kwargs):
    final_dict = {}
    for letter in range(len(args)):
        if args[letter][0] in kwargs:
            final_dict[args[letter]] = kwargs[args[letter][0]]
    sorted_dict = [f'{key} is {value} years old.' for key, value in sorted(final_dict.items(), key=lambda x: x[0])]
    return "\n".join(sorted_dict)


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
