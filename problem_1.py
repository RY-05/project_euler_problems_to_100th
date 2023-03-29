#   If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
#   The sum of these multiples is 23.
#   Find the sum of all the multiples of 3 and 5 below 1000.

sum_int = 0
for i in range(1, 10):
    if (i % 3 == 0) or (i % 5 == 0):
        # modulus operation helps check if the numbers that are ran through are multiples
        sum_int = sum_int + i
print(sum_int)
# this returns 23, consistent with the question

sum_int = 0
for i in range(1, 1000):
    # end parameter for 'for loop' is exclusive, so all positive integers < 1000 are checked
    if (i % 3 == 0) or (i % 5 == 0):
        sum_int = sum_int + i
print(sum_int)
# this returns 233168, and thus is the answer
