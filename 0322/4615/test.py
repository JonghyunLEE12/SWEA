import sys

sys.stdin = open('input.txt')
# 재밋는 오셀로 게임
from collections import deque

delta = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    arr = [[9] * (N + 1) for _ in range(N + 1)]
    arr[N // 2][N // 2] = arr[N // 2 + 1][N // 2 + 1] = 2
    arr[N // 2 + 1][N // 2] = arr[N // 2][N // 2 + 1] = 1
    lst = deque(list(map(int, input().split())) for _ in range(M))
    # 1 : 흑돌, 2: 백돌
    while lst:
        r, c, flag = lst.popleft()
        arr[r][c] = flag
        for d in delta:
            x, y = d[0], d[1]
            if 1 <= r + x <= N and 1 <= c + y <= N and arr[r + x][c + y] != flag and arr[r + x][c + y] != 9:
                tmp = []
                while True:
                    if 1 <= r + x <= N and 1 <= c + y <= N:
                        if arr[r + x][c + y] == flag:
                            for i, j in tmp:
                                arr[i][j] = flag
                            break

                        elif arr[r + x][c + y] == 9:
                            tmp.clear()
                            break

                        else:
                            tmp.append([r + x, c + y])
                            x += d[0]
                            y += d[1]
                    else:
                        tmp.clear()
                        break

    w = b = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if arr[i][j] == 1:
                b += 1
            elif arr[i][j] == 2:
                w += 1
    print(f'#{tc} {b} {w}')
