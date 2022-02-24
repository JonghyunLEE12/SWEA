import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())

# 델타
# 상 하 좌 우 대 각 선
dr = [-1,1,0,0,-1,-1,1,1]
dc = [0,0,-1,1,-1,1,-1,1]

def othello(arr):
    global M
    for _ in range(M):
        # 1 : 흑돌 2 : 백돌
        r,c,color = map(int,input().split())
        r -= 1
        c -= 1
        if not arr[r][c]:
            arr[r][c] = color
            for k in range(len(dr)):
                check_r = r + dr[k]
                check_c = c + dr[k]
                change = []
                while True:
                    # 범위 벗어나면, while문 벗어나자
                    if check_r < 0 or check_c < 0 or check_r > N -1 or check_c > N -1 :
                        change = []
                        break
                    if arr[check_r][check_c] == 0:
                        change = []
                        break
                    if arr[check_r][check_c] == color:
                        change = []
                        break
                    else:
                        change.append((check_r,check_c))
                    check_r += dr[k]
                    check_c += dc[k]
                for cr,cc in change:
                    arr[cr][cc] = color
    print(arr)
    return arr


for tc in range(1, T + 1):
    N , M = map(int,input().split())
    matrix = [[0]*N for _ in range(N)]
    for i in range(N//2-1,N//2+1):
        for j in range(N//2-1,N//2+1):
            if (i+j) % 2 :
                matrix[i][j] = 1
            else:
                matrix[i][j] = 2

    rlt = othello(matrix)
    ans = win(rlt)

    print(f'#{tc} ')

