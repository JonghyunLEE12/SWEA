import sys

sys.stdin = open('input.txt')

T = int(input())

def dfs(idx,sum_num):
    global min_num
    if sum_num >= b:
        min_num = min(min_num,sum_num)
    # sum_num 이 b 보다 커질때까지 옆 인덱스와 더해준다.
    for v in range(idx+1,n):
        if not visited[v] and sum_num + crew[v] < min_num:
            visited[v] = True
            dfs(v,sum_num+crew[v])
            visited[v] = False

for tc in range(1, T + 1):
    n,b = map(int,input().split())
    crew = list(map(int,input().split()))
    min_num = 100000000
    visited = [False] * n
    for start in range(n):
        visited[start] = True
        # 각각 인덱스를 돌면서 min_num 구하기
        dfs(start,crew[start])
        visited[start] = False
    ans = min_num - b
    print(f'#{tc} {ans}')

