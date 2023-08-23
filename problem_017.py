def ones(digit):

    dict = {
        "0": "",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine"
    }

    return dict[digit]


def tens(digit):

    dict = {
        "0": "",
        "1": "",
        "2": "twenty",
        "3": "thirty",
        "4": "forty",
        "5": "fifty",
        "6": "sixty",
        "7": "seventy",
        "8": "eighty",
        "9": "ninety"
    }

    return dict[digit]


def teens(digit):

    dict = {
        "0": "ten",
        "1": "eleven",
        "2": "twelve",
        "3": "thirteen",
        "4": "fourteen",
        "5": "fifteen",
        "6": "sixteen",
        "7": "seventeen",
        "8": "eighteen",
        "9": "nineteen"
    }

    return dict[digit]



def letter_count(lim):

    seq = ""
    
    for i in range(1, lim + 1):
        num = str(i)
        pile = []
        
        for j in range(len(num) - 1, -1, -1):
            
            if j == len(num) - 2:
                if num[j] == "1":
                    pile.append(teens(num[j + 1]))


                else:
                    pile.append(ones(num[j + 1]))
                    pile.append(tens(num[j]))


            elif len(num) == 1:
                pile.append(ones(num[j]))


            elif j == len(num) - 1 and not(len(num) == 1):
                continue


            elif j == len(num) - 3:
                if not(num[j + 2] == "0" and num[j + 1] == "0"):
                    pile.append("and")

                if not(num[j] == "0"):
                    pile.append("hundred")
                    pile.append(ones(num[j]))


            else:
                pile.append("thousand")
                pile.append("one")

            
            if j == 0:
                pile.reverse()
                
                for item in pile:
                    seq += item


    return len(seq)


print(letter_count(1000))
