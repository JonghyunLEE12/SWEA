import sys

sys.stdin = open('input.txt')

T = int(input())

def find_garo(arr):
    L = len(arr)
    cnt = 0
    ans = 0
    for i in range(L):
        for j in range(L):
            if arr[i][j] == 1:
                cnt +=1
            if arr[i][j] == 0 or j == L-1:
                if cnt == K:
                    ans +=1
                cnt = 0
    return ans

def transpose(arr):
    t_arr =[]
    for col in range(len(arr[0])):
        lst = []
        for row in range(len(arr)):
            lst.append(arr[row][col])
        t_arr.append(lst)
    return t_arr

for tc in range(1, T + 1):
    N , K = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]

    garo = find_garo(matrix)
    sero = find_garo(transpose(matrix))
    print(f'#{tc} {garo+sero}')

