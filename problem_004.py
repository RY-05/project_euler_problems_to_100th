# function to check if number is palindromic
def pali(num):

    # convert number to string for ease of manipulation
    val = str(num)

    # counter used to tally number of checks
    counter = 0

    # formula for number of checks varies
    # depending on whether the number of digits of the input
    # is odd or even
    if len(val) % 2 == 0:

        # if even, number of checks has to be
        # half of the number of digits

        # strings are zero-indexed so
        # last index checked = number of checks minus 1
        for i in range(0, int((len(val) / 2))):

            # checks if the nth digit from the front
            # is equal to the nth digit from the back
            if val[i] == val[-(i + 1)]:
                counter += 1

        # if in every check, both digits where equal
        # the number is a palindrome
        return counter == len(val) / 2

    else:

        # if odd, number of checks is 1/2(x-3)
        # where x is the number of digits
        for i in range(0, int((len(val) - 3) / 2) + 1):
            if val[i] == val[-(i + 1)]:
                counter += 1

        return counter == ((len(val) - 3) / 2) + 1


def max_pali(dig):
    return max([a * b for a in range((10 ** dig) - 1, (10 ** (dig - 1)), -1)\
            for b in range((10 ** dig) - 1, (10 ** (dig - 1)), -1) if pali(a * b)])


# this returns 9009, which is consistent with the question
print(f"{max_pali(2)} is the largest palindromic number that is a product of two {2}-digit numbers.")

# this returns 906609, the correct answer
print(f"{max_pali(3)} is the largest palindromic number that is a product of two {3}-digit numbers.")
