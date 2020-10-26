numbers = [int(x) for x in input().split()]

sum_negative = 0
sum_positive = 0

for n in numbers:
    if n < 0:
        sum_negative += n
    else:
        sum_positive += n

print(sum_negative)
print(sum_positive)

if abs(sum_negative) > sum_positive:
    print("The negatives are stronger than the positives")
elif abs(sum_negative) < sum_positive:
    print("The positives are stronger than the negatives")


