#   2520 is the smallest number that can be divided by each
#   of the numbers from 1 to 10 without any remainder.

#   What is the smallest positive number that is
#   evenly divisible by all the numbers from 1 to 20?

# //


import math as m

bound1 = 10
bound2 = 20


def min_div(bound):
    # list of all integers from 1 to bound
    nat_num_list = []
    for i in range(1, bound + 1):
        nat_num_list.append(i)

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
        multiples = []
        for j in nat_num_list:
            if j % i == 0:
                multiples.append(j)

        powers = []

        # multiples that can be expressed as power product
        x = m.ceil(m.log(multiples[-1], i))
        for n in range(1, x + 1):
            if i ** n in multiples:
                powers.append(n)

        # greatest power product
        max_powers.append(max(powers))

    # multiply all the primes (to their greatest powers) with each other
    prod = 1
    for i in range(0, len(primes)):
        prod *= primes[i] ** max_powers[i]

    return prod


# when bound is 10, returns 2520, which is consistent with the question
print("The smallest possible number that is evenly divisible by all integers from 1 to "\
      + str(bound1) + " is " + str(min_div(bound1)) + ".")

# when bound = 20, returns 232792560, the correct answer
print("The smallest possible number that is evenly divisible by all integers from 1 to "\
      + str(bound2) + " is " + str(min_div(bound2)) + ".")
