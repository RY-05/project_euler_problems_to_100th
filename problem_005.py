import math as m

bound1 = 10
bound2 = 20


def min_div(bound):
    # list of all integers from 1 to bound
    nat_num_list = [i for i in range(1, bound + 1)]

    # list of primes between 1 and bound
    primes = []
    for i in range(1, bound + 1):
        factors = []
        for j in range(1, i + 1):
            if i % j == 0:
                factors.append(j)
        if len(factors) == 2:
            primes.append(i)

    max_powers = []
    for i in primes:

        # multiples of each prime number
        multiples = [j for j in nat_num_list if j % i == 0]

        # multiples that can be expressed as power product
        x = m.ceil(m.log(multiples[-1], i))
        powers = [n for n in range(1, x + 1) if (i ** n in multiples)]

        # greatest power product
        max_powers.append(max(powers))

    # multiply all the primes (to their greatest powers) with each other
    prod = 1
    for i in range(0, len(primes)):
        prod *= primes[i] ** max_powers[i]

    return prod


# returns 2520, which is consistent with the question
print(f"The smallest possible number that is evenly divisible "
      f"by all integers from 1 to {bound1} is {min_div(bound1)}.")

# returns 232792560, the correct answer
print(f"The smallest possible number that is evenly divisible "
      f"by all integers from 1 to {bound2} is {min_div(bound2)}.")
