import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N = int(input())

    # 달팽이가 이동할 리스트
    snail = [ [0]*N for _ in range(N)]

    # 이동 방향 : 우 -> 하 -> 좌 -> 상
    dr=[0,1,0,-1]
    dc=[1,0,-1,0]

    # 달팽이 시작 과 진행 방향
    row = 0
    col = 0
    direction = 0

    for i in range(1,N*N+1):
        # 달팽이가 이동한 공간을 i 로 바꿔줌
        snail[row][col] = i
        # 방향 쪽으로 이동
        row += dr[direction]
        col += dc[direction]

        if row < 0 or row >=N or col < 0 or col >=N or snail[row][col] != 0:
            row -= dr[direction]
            col -= dc[direction]

            direction = (direction+1)%4

            row += dr[direction]
            col += dc[direction]

    print(f'#{tc}')
    for k in snail:
        print(*k)

