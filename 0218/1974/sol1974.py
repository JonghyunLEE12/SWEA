import sys

sys.stdin = open('input.txt')

T = int(input())
def garo(arr):
    L = len(arr)
    for row in range(L):
        num_list=[]
        for col in range(L-1):
            if arr[row][col] not in num_list:
                num_list.append(arr[row][col])
            else :
                return False
    return True
def sero(arr):
    L = len(arr)
    for col in range(L):
        num_list =[]
        for row in range(L-1):
            if arr[row][col] not in num_list:
                num_list.append(arr[row][col])
            else:
                return False
    return True
def three(arr):
    L = len(arr)
    for i in range(L-3):
        for j in range(L-3):
            num_list =[]
            for a in range(3):
                for b in range(3):
                    if arr[a][b] not in num_list:
                        num_list.append(arr[a][b])
                    else:
                        return False
    return True

for tc in range(1, T + 1):
    arr = [list(map(int,input().split())) for _ in range(9)]
    rlt_garo = garo(arr)
    rlt_sero = sero(arr)
    rlt_theree = three(arr)
    if rlt_garo and rlt_sero and rlt_theree :
        rlt = 1
    else :
        rlt = 0
    print(f'#{tc} {rlt}')

