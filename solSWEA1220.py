import sys

sys.stdin = open('input (10).txt')

T = 10

for tc in range(1, T + 1):
    N = int(input())
    mag = []
    for i in range(N):
        mag.append(list(map(int,input().split())))

    cnt = 0
    for i in range(N):
        check = 0
        for j in range(N):
            if mag[j][i] == 1 and check == 0:
                check = 1
            elif mag[j][i] == 2 and check == 1:
                cnt += 1
                check = 0

    print(f'#{tc} {cnt}')

