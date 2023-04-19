#   The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#   Find the sum of all the primes below two million.

#   //


import math as m

lim1 = 10
lim2 = 2000000


def primes(x):

    # set of primes
    list = []

    for i in range(1, x):

        # primes have only two factors, one and itself
        count = 2

        # if a number has zero factors between 2 and its square root, it is prime
        for j in range(2, m.floor(m.sqrt(i)) + 1):
            if i % j == 0:
                count += 1

        if count == 2 and i != 1:
            list.append(i)


    return list


sum = 0
for i in primes(lim1):
    sum += i
print(sum)


sum = 0
for i in primes(lim2):
    sum += i
print(sum)
