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


# This returns 17, which is consistent with the question
print(f"The sum of all primes below {lim1} is {sum([i for i in primes(lim1)])}.")

# This returns 142913828922, the correct answer
print(f"The sum of all primes below {lim2} is {sum([i for i in primes(lim2)])}.")
