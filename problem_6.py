# The sum of the squares of the first ten natural numbers is

# 1^2 + 2^2 + ... + 10^2 = 385.

# The square of the sum of the first ten natural numbers is

# (1 + 2 + ... + 10)^2 = 3025.

# Hence the difference between the sum of the squares of the first ten
# natural numbers and the square of the sum is 3025 - 385 = 2640.

# Find the difference between the sum of the squares
# of the first one hundred natural numbers and the square of the sum.

# /


lim = 100


# function returns the sum of the squares of all natural numbers
# from 1 to lim, inclusive
def sum_sqr(a):
    sum = 0
    for i in range(1, lim + 1):
        sum += i ** 2

    return sum

print(sum_sqr(lim))


# function returns the square of the sum of all natural numbers
# from 1 to lim, inclusive
def sqr_sum(a):
    sum = 0
    for i in range(1, lim + 1):
        sum += i

    return sum ** 2

print(sqr_sum(lim))

print("The difference between the sum of the squares and the square of the sum is " + str(sqr_sum(lim) - sum_sqr(lim)) + ".")
# programme returns 25164150 which is the final answer
