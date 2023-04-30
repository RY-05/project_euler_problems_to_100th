def pythag_trip(num):
    coprime_pairs = []

    # generating coprime pairs
    # arbitrarily chose 100 as stop value
    for num1 in range(1, 100):
        num1_factors = []
        for i in range(1, num1 + 1):
            if num1 % i == 0:
                num1_factors.append(i)

        for num2 in range(1, 100):
            num2_factors = []
            for j in range(1, num2 + 1):
                if num2 % j == 0:
                    num2_factors.append(j)

            # a coprime pair a, b is
            # defined by hcf(a, b) = 1
            shared_factors = []
            for item in num1_factors:
                if item in num2_factors:
                    shared_factors.append(item)

            if max(shared_factors) == 1:
                coprime_pairs.append([num1, num2])

    # sorting each array [m, n]
    # such that m < n
    for item in coprime_pairs:
        item = item.sort()

    # sorting the 2D array
    coprime_pairs.sort()

    # removing duplicate items
    for item in coprime_pairs:
        if coprime_pairs.count(item) > 1:
            while coprime_pairs.count(item) > 1:
                coprime_pairs.remove(item)

    trip_list = []

    # generating pythagorean triples
    for item in coprime_pairs:
        a = (item[1] ** 2) - (item[0] ** 2)
        b = 2 * item[0] * item[1]
        c = (item[0] ** 2) + (item[1] ** 2)

        if (num % (a + b + c) == 0) and (a + b + c != 0):
            new_a = a * (num / (a + b + c))
            new_b = b * (num / (a + b + c))
            new_c = c * (num / (a + b + c))

            trip_list.append([new_a, new_b, new_c])

    for item in trip_list:
        if 0.0 not in item:
            return item[0] * item[1] * item[2]


# returns 31875000, the correct answer
print(pythag_trip(1000))
