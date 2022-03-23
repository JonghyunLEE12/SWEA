import sys

sys.stdin = open('input.txt')

T = int(input())

def dfs(idx,sum_num):
    global min_num
    # 직원들의 키의 합이 선반의 길이를 넘어갔을 때 return
    if sum_num >= b:
        min_num = min(min_num,sum_num)
        return
    for next in range(idx+1,n):
        if not visited[next] and sum_num + crew[next] < min_num:
            visited[next] = True
            dfs(next,sum_num+crew[next])
            visited[next] = False

for tc in range(1, T + 1):
    n,b = map(int,input().split())
    crew = list(map(int,input().split()))
    # 크루원의 수 만큼 생성
    visited = [False] * n

    min_num = 1000000000
    for start in range(n):
        visited[start] = True
        dfs(start,crew[start])
        visited[start] = False
    ans = min_num - b
    print(f'#{tc} {ans}')

