def div(num):
    list = [1, num]
    for i in range(2, num//2 + 1):
        if num % i == 0:
            list.append(i)

    return len(list)


def func(divs):
    tri = 0
    add = 0

    while div(tri) < divs:
        tri += add
        add += 1

    return tri


print(func(500))
# 76576500