lim1 = 10
lim2 = 100


# sum of squares, 1 to limit inclusive
def sum_sqr(a):
    return sum(i ** 2 for i in range(1, a + 1))


# square of the sum
def sqr_sum(a):
    return sum(i for i in range(1, a + 1)) ** 2


# returns 2640, which is consistent with the question
print(f"The difference between the sum of the squares and "
      f"the square of the sum of all natural numbers up to "
      f"{lim1} is {sqr_sum(lim1) - sum_sqr(lim1)}.")

# returns 25164150, the correct answer
print(f"The difference between the sum of the squares and "
      f"the square of the sum of all natural numbers up to "
      f"{lim2} is {sqr_sum(lim2) - sum_sqr(lim2)}.")
