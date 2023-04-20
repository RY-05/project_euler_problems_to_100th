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
            if val[i] == val[-(i+1)]:
                counter += 1

        # if in every check, both digits where equal
        if counter == len(val) / 2:

            # the number is a palindrome
            return True

        else:
            return False

    else:

        # if odd, number of checks is 1/2(x-3)
        # where x is the number of digits
        for i in range(0, int((len(val) - 3) / 2) + 1):
            if val[i] == val[-(i+1)]:
                counter += 1

        if counter == ((len(val) - 3) / 2) + 1:
            return True

        else:
            return False


two_dig_pali_list = []

for a in range(99, 10, -1):
    for b in range(99, 10, -1):
        if pali(a*b):
            two_dig_pali_list.append(a*b)
            
# this returns 9009, which is consistent with the question
print(str(max(two_dig_pali_list)), "is the largest palindromic number that is a product of two two-digit numbers.")


three_dig_pali_list = []

for a in range(999, 99, -1):
    for b in range(999, 99, -1):
        if pali(a*b):
            three_dig_pali_list.append(a*b)
            
# this returns 906609, the correct answer
print(str(max(three_dig_pali_list)), "is the largest palindromic number that is a product of two three-digit numbers.")
