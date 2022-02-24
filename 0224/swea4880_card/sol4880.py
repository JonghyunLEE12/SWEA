import sys

sys.stdin = open('input.txt')

T = int(input())

def RCP(idx_i,idx_j):
    x,y = card[idx_i-1],card[idx_j-1]
    if x == y:
        return idx_i
    elif x == 1:
        if y == 3:
            return idx_i
        elif y == 2:
            return idx_j
    elif x == 2:
        if y == 1:
            return idx_i
        elif y == 3:
            return idx_j
    elif x == 3:
        if y == 2:
            return idx_i
        elif y == 1:
            return idx_j


def cardgame(start,end):
    if start == end:
        return start
    else:
        middle = (start+end)//2
        i = cardgame(start,middle)
        j = cardgame(middle+1,end)
        return RCP(i,j)


for tc in range(1, T + 1):
    N = int(input())
    card = list(map(int,input().split()))

    print(f'#{tc} {cardgame(1,N)}')

