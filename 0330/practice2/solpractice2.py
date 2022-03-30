import sys

sys.stdin = open('input.txt')

T = 1

def dfs(start):
    if sum(rlt) == 10:
        print(*rlt)
        return rlt
    for next in range(start,len(numbers)):
        if visited[next] == 0:
            visited[next] = 1
            rlt.append(next)
            dfs(next)
            rlt.pop()
            visited[next] = 0


for tc in range(1, T + 1):
    numbers = list(map(int,input().split()))
    visited = [0] * (len(numbers)+1)
    for start in range(1,len(numbers)+1):
        rlt = [start]
        visited[start] = 1
        dfs(start)
        visited[start] = 0
    print(f'#{tc}')

