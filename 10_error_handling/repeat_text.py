try:
    first_word = input()
    times = int(input())
    output = first_word * times
    print(output)
except ValueError:
    print("Variable times must be an integer")

