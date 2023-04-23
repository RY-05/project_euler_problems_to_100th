a = 3
b = 5
val1 = 10
val2 = 1000


def sum_multiples(num1, num2, limit):
    return sum([i for i in range(1, limit) if (i % num1 == 0) or (i % num2 == 0)])


# this returns 23, which is consistent with the question
print(f"The sum of all the multiples of {a} and {b} below {val1} is {sum_multiples(a, b, val1)}.")

# this returns 233168, the correct answer
print(f"The sum of all the multiples of {a} and {b} below {val2} is {sum_multiples(a, b, val2)}.")

