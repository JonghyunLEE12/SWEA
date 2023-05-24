import math

def solution(n, number):
    possible_val = dict()   # key: count, val: available value
    done = set()
    possible_val[1] = set([n])
    if n == number:
        return 1
    done.add(n)

    x = n
    for idx in range(2,9):
        possible_val[idx] = set()
        x *= 10
        x += n
        if number == x:
            return idx
        possible_val[idx].add(x)
        done.add(x)

    for idx in range(2,9):
        for jdx in range(1,math.ceil(idx/2)+1):
            prev1 = possible_val[jdx]
            prev2 = possible_val[idx-jdx]
            for val1 in prev1:
                for val2 in prev2:
                    for odx in range(6):
                        if odx == 1:
                            check = val1*val2
                        elif odx == 2:
                            check = val1-val2
                        elif odx == 3:
                            check = val1//val2
                        elif odx == 4:
                            check = val2-val1
                        elif odx == 5:
                            check = val2//val1
                        else:
                            check = val1+val2
                        if check in done or check == 0:
                            continue
                        possible_val[idx].add(check)
                        done.add(check)
                        if check == number:
                            return idx

    return -1
