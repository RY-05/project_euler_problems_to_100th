# set variable for highest value in sequence
lim = 4000000
fibo = [1, 2]


def fibonacci(limit):
    # checking that the last term in the sequence is lesser than four million
    while fibo[-1] < limit:

        # adding last two terms in the sequence for the next term
        fibo.append(fibo[-1] + fibo[-2])

        if fibo[-1] > lim:
            fibo.pop()
            break

        # recursive statement
        else:
            fibonacci(limit)

    return fibo


# this returns 4613732, the correct answer
print(f"The sum of the even-valued terms, whose values do not exceed {lim}, "
      f"is {sum([i for i in fibonacci(lim) if (i % 2 == 0)])}.")
