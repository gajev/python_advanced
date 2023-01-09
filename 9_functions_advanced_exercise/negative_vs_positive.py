def positive_negative(*args):
    positives = 0
    negatives = 0
    for number in args:
        if number > 0:
            positives += number
        else:
            negatives += number
    return positives, negatives


numbers = [int(x) for x in input().split()]
positive_sum, negative_sum = positive_negative(*numbers)
print(negative_sum)
print(positive_sum)
if positive_sum > abs(negative_sum):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")
