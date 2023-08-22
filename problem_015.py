def factorial(num):
    product = 1
    for i in range(2, num + 1):
        product *= i

    return product


val = factorial(40) / (factorial(20) * factorial(20))
print(val)
