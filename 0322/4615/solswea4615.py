import sys

sys.stdin = open('input.txt')

from collections import deque

T = int(input())
# 상 하 좌 우 대 각 선
dr = [-1,1,0,0,1,-1,1,-1]
dc = [0,0,-1,1,1,1,-1,-1]



def bfs():
    queue = deque(list(map(int,input().split())) for _ in range(M))
    while queue:
        r,c,flag = queue.popleft()
        arr[r][c] = flag
        for i in range(len(dr)):
            new_r = r + dr[i]
            new_c = c + dc[i]
            if 1 <= new_r <= N and 1<= new_c <= N and arr[new_r][new_c] != flag and arr[new_r][new_c] != 0:
                tmp = []
                while True:
                    if 1 <= new_r <= N and 1 <= new_c <= N:
                        # 같은 돌 색을 만나면, 색깔 바꾸기
                        if arr[new_r][new_c] == flag:
                            for i, j in tmp:
                                arr[i][j] = flag
                            break

                        # 돌이 없을 때
                        elif arr[new_r][new_c] == 0:
                            tmp.clear()
                            break

                        else:
                            # 한 방향 탐색
                            tmp.append([new_r, new_c])
                            new_r = new_r + dr[i]
                            new_c = new_c + dc[i]
                    # 범위 벗어 났을 때
                    else:
                        tmp.clear()
                        break


for tc in range(1, T + 1):
    N,M = map(int,input().split())

    arr = [[0] * (N + 1) for _ in range(N + 1)]
    arr[N // 2][N // 2] = arr[N // 2 + 1][N // 2 + 1] = 2
    arr[N // 2 + 1][N // 2] = arr[N // 2][N // 2 + 1] = 1

    bfs()
    b,w,=0,0
    for i in range(N+1):
        for j in range(N+1):
            if arr[i][j] == 1:
                b +=1
            elif arr[i][j] == 2:
                w += 1


    print(f'#{tc} {b} {w}')

