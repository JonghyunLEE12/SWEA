import sys

sys.stdin = open('input.txt')

# 해당 방향으로 움직였을 때, 좌표값이 어떻게 달라 지는가?
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def robot(x,y,d):
    global cnt
    # x , y 가 0 이면 위치 2 로 변경후 cnt 증가
    if maps[x][y] == 0:
        maps[x][y] = 2
        cnt += 1
    for _ in range(len(dx)):
        # 왼쪽을 확인
        new_d = (d+3)%4
        new_x = x + dx[new_d]
        new_y = y + dy[new_d]
        if maps[new_x][new_y] == 0:
            robot(new_x,new_y,new_d)
            return
        # 왼쪽을 계속 탐색해서 청소할 공간이 없을때, 방향 변경
        d = new_d
    # 이제 뒤를 확인해 보자
    new_d = (d+2) % 4
    new_x = x + dx[new_d]
    new_y = y + dy[new_d]
    if maps[new_x][new_y] == 1:
        return
    robot(new_x , new_y , d)

N , M = map(int,input().split())
x , y , d = map(int,input().split())
maps=[]
for i in range(N):
    maps.append(list(map(int,input().split())))
cnt = 0
robot(x,y,d)
print(cnt)
