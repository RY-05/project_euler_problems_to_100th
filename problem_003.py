import math as m

num1 = 13195
num2 = 600851475143

def prime_bool(x):
    # variable counts factors of x, besides 1 and x
    fac_count = 2

    # check for factors between 2 and the square root
    k = m.floor(m.sqrt(x))
    for i in range(2, k + 1):
        if x % i == 0:
            fac_count += 1

    # primes have no factors between 2 and their square root
    if fac_count == 2 and x != 1:
        return True

    else:
        return False


def factors(x):
    list = []
    for i in range(1, (x // 2) + 1):
        if x % i == 0:
            list.append(i)
    list.append(x)

    return list


prime_facs = []
for i in factors(num1):
    if prime_bool(i):
        prime_facs.append(i)

# this returns 5, 7, 13 and 29, which is consistent with the question
print("The prime factors of " + str(num1) + " are " + str(prime_facs) + ".")
print("The largest prime factor of " + str(num1) + " is " + str(max(prime_facs)) + ".")


prime_facs = []
for i in factors(num2):
    if prime_bool(i):
        prime_facs.append(i)

print("The prime factors of " + str(num1) + " are " + str(prime_facs) + ".")
print("The largest prime factor of " + str(num2) + " is " + str(max(prime_facs)) + ".")
