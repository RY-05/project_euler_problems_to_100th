# number of adjacent digits
n1 = 4
n2 = 13

data = "73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450"


def adj_prod(x):

    # set of products
    list1 = []

    # 2D list of sets of x adjacent numbers
    list2 = []

    # shifting starting position of product calculation
    for i in range(0, len(data) - x):
        prod = 1
        # operation for product of x adjacent digits
        for j in range(0, x):
            prod *= int(data[i + j])

        list1.append(prod)

        # stores x adjacent digits
        temp_list = []

        # composing list of digits in product
        for k in range(0, x):
            temp_list.append(data[i + k])

        list2.append(temp_list)

    return list1, list2


# calling function as tuple
prod_list, adj_num_list = adj_prod(n1)

# index of each set corresponds with index of product of set
pos = prod_list.index(max(prod_list))

print(f"The {n1} adjacent digits in the 1000-digit number "
      f"that have the greatest product are {[int(i) for i in (adj_num_list[pos])]}, "
      f"producing {prod_list[pos]}.")

print('')

prod_list, adj_num_list = adj_prod(n2)
pos = prod_list.index(max(prod_list))

print(f"The {n2} adjacent digits in the 1000-digit number "
      f"that have the greatest product are {[int(i) for i in (adj_num_list[pos])]}, "
      f"producing {prod_list[pos]}.")
