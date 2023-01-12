number = int(input())
matrix = []
first_diagonal = []
second_diagonal = []
for _ in range(number):
    matrix.append(list(int(x) for x in input().split()))
for i in range(len(matrix)):
    first_diagonal.append(matrix[i][i])
    second_diagonal.append(matrix[i][len(matrix) - i - 1])
first_sum = sum(first_diagonal)
second_sum = sum(second_diagonal)
result = first_sum - second_sum
print(abs(result))