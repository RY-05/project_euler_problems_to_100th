# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10,001st prime number?

# /


import math as m

# val = int(input("Enter n such that you receive the nth prime number."))
val = 10001


def prime_nth_term(a):
    # used to check the nth term, within the sequence of prime numbers
    primes_passed = 0

    # positive integer to check if prime
    i = 0

    # stops checking for primes when nth term is reached
    while primes_passed < a:
        i += 1

        # filling list of factors of i
        temp_list = []
        for j in range(1, m.floor(m.sqrt(i)) + 1):
            if i % j == 0:
                temp_list.append(j)
        temp_list.append(i)

        # prime numbers have two distinct factors: 1 and themselves
        if len(temp_list) == 2 and (temp_list[0] != temp_list[-1]):
            primes_passed += 1
            # print(str(i) + " is the " + str(primes_passed) + "th prime number.")

    if primes_passed == a:
        return i

# main programme
if len(str(val)) == 1:
    if str(val)[-1] == "1":
        print("The " + str(val) + "st prime number is " + str(prime_nth_term(val)) + ".")

    elif str(val)[-1] == "2":
        print("The " + str(val) + "nd prime number is " + str(prime_nth_term(val)) + ".")

    elif str(val)[-1] == "3":
        print("The " + str(val) + "rd prime number is " + str(prime_nth_term(val)) + ".")

    else:
        print("The " + str(val) + "th prime number is " + str(prime_nth_term(val)) + ".")


else:
    if str(val)[-2] != "1":
        if str(val)[-1] == "1":
            print("The " + str(val) + "st prime number is " + str(prime_nth_term(val)) + ".")

        elif str(val)[-1] == "2":
            print("The " + str(val) + "nd prime number is " + str(prime_nth_term(val)) + ".")

        elif str(val)[-1] == "3":
            print("The " + str(val) + "rd prime number is " + str(prime_nth_term(val)) + ".")

        else:
            print("The " + str(val) + "th prime number is " + str(prime_nth_term(val)) + ".")

    else:
        print("The " + str(val) + "th prime number is " + str(prime_nth_term(val)) + ".")
        
# prints 104743 which is the correct answer
