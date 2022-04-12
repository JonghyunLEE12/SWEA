import sys
from collections import deque
from pprint import pprint
sys.stdin = open('input8.txt')

def bfs():
    global rlt
    while True:
        q = deque()
        visited = [[0] * M for _ in range(N)]
        cnt = 0     #빙하수
        rlt += 1    #시간
        for r in range(N):
            for c in range(M):

                if matrix[r][c]:
                    # 상하좌우 돌면서 범위내, 위아래에 0이 있는 경우 위치에 append
                    for k in range(4):
                        rr, cc = r + dr[k], c + dc[k]
                        if 0 <= rr < N and 0 <= cc < M and matrix[rr][cc] == 0:
                            q.append((r, c))

                #빙하 붙어있는지 확인하는 부분
                if matrix[r][c] and not visited[r][c]:
                    qq = deque()
                    qq.append((r, c))
                    cnt += 1
                    visited[r][c] = cnt
                    while qq:
                        x, y = qq.popleft()
                        for k in range(4):
                            rr, cc = x + dr[k], y + dc[k]
                            if 0 <= rr < N and 0 <= cc < M and matrix[rr][cc] and not visited[rr][cc]:
                                visited[rr][cc] = cnt
                                qq.append((rr, cc))



        #위에서 0이 붙어있는 애들 녹여주기
        while q:
            rrr, ccc = q.pop()
            if matrix[rrr][ccc] > 0:
                matrix[rrr][ccc] -= 1

        #matrix[r][c]가 값이 하나도 없으면 cnt =0
        if cnt ==0:
            rlt = 0
            return

        #얼음이 2개이상 분리되면 반환 지난시간 -1
        if cnt >=2:
            rlt -= 1
            return

N, M = map(int,input().split()) #N 행, M 열
matrix = [list(map(int, input().split())) for _ in range(N)]

dr,dc = [-1,1,0,0],[0,0,-1,1]   #상하좌우
rlt = 0
bfs()
print(rlt)