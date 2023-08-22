def digit_sum(base, power):

    digits = str(base ** power)
    sum = 0

    for i in range(len(digits)):
        sum += int(digits[i])

    return sum

print(digit_sum(2, 1000))
