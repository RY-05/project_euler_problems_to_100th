// The prime factors of 13195 are 5, 7, 13 and 29.

// What is the largest prime factor of the number 600851475143 ?


// Write program in C++
// Because Python is too inefficient for extremely large values


// Python code

/*
num = 13195


# function to check if given value is prime
def prime(val):

    # list for numbers that are factors of given value
    divisibles = []

    # running through numbers from 1 to half of given value to check if each of them are a factor
    # stop at half because it is impossible for a factor to be greater than a half of the given value
    for number in range(1, ((val + 1) // 2) + 1):
        if val % number == 0:
            divisibles.append(number)

    # evident that given value would be a factor of the given value
    # skip through checking if values greater than half are factors, certainly not
    divisibles.append(val)

    # primes have only two factors: one and itself
    if len(divisibles) == 2 and divisibles[-1] != 1:
        return True
    else:
        return False


# generate list of factors of num
factors = []

for i in range(1, (num + 1) // 2):
    if num % i == 0:
        factors.append(i)
factors.append(num)

print(factors)

# generate list of prime factors of num
prime_factors = []

for j in factors:
    if prime(j):
        prime_factors.append(j)

print(prime_factors)

# print largest prime factor of num
print(max(prime_factors))
*/
