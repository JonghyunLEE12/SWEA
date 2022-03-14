import sys

sys.stdin = open('input.txt')

'''
첫째 줄에는 사각형 모양 판의 세로와 가로의 길이가 양의 정수로 주어진다. 
세로와 가로의 길이는 최대 100이다. 판의 각 가로줄의 모양이 윗 줄부터 차례로 둘째 줄부터 마지막 줄까지 주어진다. 
치즈가 없는 칸은 0, 치즈가 있는 칸은 1로 주어지며 각 숫자 사이에는 빈칸이 하나씩 있다.
'''
from collections import deque

n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]

def bfs():
    queue = deque()
    queue.append((0,0))
    stack = [[0]*(m) for _ in range(n)]
    # 델타 상하좌우
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    cnt = 0
    while queue:
        r,c = queue.popleft()
        for i in range(4):
            new_r = r + dr[i]
            new_c = c + dc[i]
            if 0<= new_r < n and 0<= new_c < m:
                if matrix[new_r][new_c] == 0 and stack[new_r][new_c] == 0:
                    stack[new_r][new_c] = 1
                    queue.append((new_r,new_c))
                if matrix[new_r][new_c] == 1:
                    matrix[new_r][new_c] = 0
                    cnt += 1
                    stack[new_r][new_c] = 1
    return cnt

rlt = []
time = 0
while True:
    cnt = bfs()
    rlt.append(cnt)
    if cnt == 0:
        break
    time += 1
print(time)
print(rlt[-2])
print(rlt)