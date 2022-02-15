import sys
sys.stdin = open('input.txt')

T = 10

def ladder(r,c):
    # 델타
    # 좌 우 상 ( 좌 , 우 를 먼저 탐색 후 위로 올라가야함 )
    dr = [0, 0, -1]
    dc = [-1, 1, 0]

    direction = 0

    while True:
        if r <= 0:                                      # r 이 0이 될 때 종료
            break
        new_r = r + dr[direction]                       # new_r 에 왼쪽부터 탐색
        new_c = c + dc[direction]
        if 0 <= new_r < 100 and 0<= new_c < 100:        # new_r 과 new_c가 범위 안쪽에 있는 경우,
            if ladders[new_r][new_c] == 1:              # 만약 좌,우,상에 1이 있는 경우
                r = new_r                               # r , c 값 변경
                c = new_c
                ladders[new_r][new_c] = 0               # 이미 지나간 곳은 0 으로 바꿔줌
        direction = (direction + 1 ) % 3                # direction 은 항상 1 , 2 , 3 만 나옴

    return c




for tc in range(1, T + 1):
    N = int(input())
    ladders = [list(map(int,input().split())) for _ in range(100)]

    # 2 찾기
    x = 99
    for i in range(100):
        if ladders[99][i] == 2:
            y = i
    print(f'#{tc} {ladder(x,y)}')
