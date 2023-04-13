# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all the numbers from 1 to 20?

# //


import math as m

bound = 20

# list of all integers from 2 to bound
nat_num_list = []
for i in range(1, bound + 1):
    nat_num_list.append(i)


# list of primes between 2 and bound
primes = []
for i in range(1, bound + 1):
    factors = []
    for j in range(1, i + 1):
        if i % j == 0:
            factors.append(j)
    if len(factors) == 2:
        primes.append(i)


# find the highest power product of each prime by finding the multiples of each one
# and then finding the largest of those multiples that can be expressed as a power product of the prime
max_powers = []
for i in primes:
    multiples = []
    for j in nat_num_list:
        if j % i == 0:
            multiples.append(j)

    powers = []

    x = m.ceil(m.log(multiples[-1], i))
    for n in range(1, x + 1):
        if i**n in multiples:
            powers.append(n)

    max_powers.append(max(powers))

    
# multiply all the primes (to their greatest powers) with each other
prod = 1
for i in range(0, len(primes)):
    prod *= primes[i] ** max_powers[i]

    
# when bound = 20, returns 232792560 and thus is the answer
print("The smallest possible number that is evenly divisible by all integers from 1 to " + str(bound) + " is " + str(prod) + ".")
