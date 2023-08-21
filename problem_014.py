def collatz(lim):

    terms_list = []

    for i in range(1, lim):
        num = i
        terms = 1

        while num != 1:

            if num % 2 == 0:
                num /= 2
                terms += 1

            else:
                num *= 3
                num += 1
                terms += 1

        terms_list.append(terms)

    return terms_list.index(max(terms_list)) + 1


print(collatz(10**6))
