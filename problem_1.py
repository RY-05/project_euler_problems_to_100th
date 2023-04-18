#   If we list all the natural numbers below 10 
#   that are multiples of 3 or 5, we get 3, 5, 6 and 9.
#   The sum of these multiples is 23.
#   Find the sum of all the multiples of 3 and 5 below 1000.

# //


a = 3
b = 5
val1 = 10
val2 = 1000


def sum_multiples(num1, num2, limit):
    total = 0
    for i in range(1, limit):
        # modulus operation helps check if the numbers
        # that are ran through are multiples
        if (i % num1 == 0) or (i % num2 == 0):
            total += i

    return total


# this returns 23, which is consistent with the question
print("The sum of all the multiples of " + str(a) + " and "\
      + str(b) + " below " + str(val1) + " is "\
      + str(sum_multiples(a, b, val1)) + ".")

# this returns 233168, the correct answer
print("The sum of all the multiples of " + str(a) + " and "\
      + str(b) + " below " + str(val2) + " is "\
      + str(sum_multiples(a, b, val2)) + ".")
