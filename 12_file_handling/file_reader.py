file = open("./numbers.txt", "r")
sum_of_numbers = 0
for number in file:
    sum_of_numbers += int(number)
print(sum_of_numbers)
file.close()