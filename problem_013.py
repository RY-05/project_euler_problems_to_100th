def func(file, digits=10):

    sum = 0

    with open(file, 'r') as f:

        for line in f:
            sum += int(line)

    return int(str(sum)[0:digits])


print(func('problem_013.txt'))
