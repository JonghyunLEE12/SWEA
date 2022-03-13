import sys

sys.stdin = open('input.txt')

'''
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 
다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 
각각의 수들은 붙어서 입력으로 주어진다.
'''
from collections import deque

n,m  = map(int,input().split())
matrix = [ list(map(int,input())) for _ in range(n)]
def bfs(r,c):
    # 델타 : 상 하 좌 우
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    queue = deque()
    queue.append((r,c))
    while queue:
        r,c = queue.popleft()
        for i in range(4):
            new_r = r + dr[i]
            new_c = c + dc[i]

            if 0 > new_r or 0 > new_c or new_r >= n or new_c >= m:
                continue

            if matrix[new_r][new_c] == 0:
                continue

            if matrix[new_r][new_c] == 1:
                matrix[new_r][new_c] = matrix[r][c] + 1
                queue.append((new_r,new_c))

    return matrix[n-1][m-1]



print(bfs(0,0))
