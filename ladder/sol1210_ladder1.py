import sys
sys.stdin = open('input.txt')

T = 10
def ladder(c):
    r = 99                              # r의 초기 값은 99
    # 델타
    # 좌 우 상
    dr=[0,0,-1]
    dc=[-1,1,0]
    direction = 0                       # 방향 0
    while True:
        if r <= 0:                      # r이 0 보다 작거나 같으면 break
            break
        new_r = r + dr[direction]       # direction 방향 탐색
        new_c = c + dc[direction]
        # new_r 과 new_c 인덱스 체크
        if 0<= new_r < 100 and 0<= new_c < 100:     # new_r 과 new_c 가 범위 안에 있는 경우
            if ladders[new_r][new_c] == 1:          # direction 방향에 1이 있을 때
                r = new_r                           # r 값 변경
                c = new_c                           # c 값 변경
                ladders[new_r][new_c] = 0           # 갔던 길은 0으로 초기화
        direction = (direction + 1) % 3             # direction 은 0, 1, 2 만 나와야함 ( 달팽이 )
    return c

def find_2(arr):
    for i in range(len(arr)):
        if arr[99][i] == 2:
            y = i
    return y

for tc in range(1, T + 1):
    N = int(input())
    ladders = [list(map(int,input().split())) for _ in range(100)]
    rlt = ladder(find_2(ladders))
    print(f'#{tc} {rlt}')
