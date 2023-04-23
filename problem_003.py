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
    return [i for i in range(1, (x // 2) + 1) if (x % i == 0)]


def prime_facs(x):
    return [i for i in factors(x) if prime_bool(i)]


# this returns 5, 7, 13 and 29, which is consistent with the question
print(f"The prime factors of {num1} are {prime_facs(num1)}, "
      f"of which {max(prime_facs(num1))} is the largest.")

# this returns 6857, the correct answer
print(f"The prime factors of {num2} are {[prime_facs(num2)]}, "
      f"of which {max(prime_facs(num2))} is the largest.")
