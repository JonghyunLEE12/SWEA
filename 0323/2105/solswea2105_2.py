import sys

sys.stdin = open('input.txt')

T = int(input())

#델타
dr = [1,1,-1,-1]
dc = [1,-1,-1,1]


# DFS 함수 구현
def dfs(r, c, d, cnt):
    global ans

    # 현재 노드에서 우하단 방향으로 시작해서
    # 시계방향으로 탐색한다고 가정하면,탐색 방향은 두 가지로 고정됨
    # 예를들어 우하단으로 시작 -> 다음 탐색 방향은 우하단 or 좌하단
    # 이렇게 해도 모든 탐색의 경우의 수를 체크할 수 있음이 보장됨
    for i in range(2):
        # 방향 설정
        tmp_d = (d + i) % 4
        # 다음칸
        rr, cc = r + dr[tmp_d], c + dc[tmp_d]
        # 우하단 방향으로 시작해서 시계방향으로
        # 시작 칸으로 돌아온다고 가정했으므로
        # 시작 칸의 행의 위쪽은 탐색할 필요 없음
        if start_r <= rr < n and 0 <= cc < n:
            # 종료 조건
            # 2개 이상의 디저트를 먹고 시작칸으로 돌아왔을 경우
            if cnt != 0 and rr == start_r and cc == start_c:
                ans = max(ans, cnt + 1)
                return
            # 다음칸 탐색
            # 만약 다음칸의 디저트를 먹지 않았다면
            if array[rr][cc] not in dessert:
                # 디저트 리스트에 추가
                dessert.append(array[rr][cc])
                # DFS 재귀 호출
                dfs(rr, cc, tmp_d, cnt + 1)
                # 백트래킹 해야하므로
                # 리스트에 넣어주었던 디저트 제거
                # 스택이므로 마지막 원소를 빼주면 됨
                dessert.pop()

for tc in range(1, T + 1):
    n = int(input())
    array = [list(map(int,input().split())) for _ in range(n)]

    ans = 0
    for r in range(n-1):
        for c in range(1,n-1):
            dessert = [array[r][c]]
            start_r,start_c = r,c
            dfs(r,c,0,0)
    print(ans)
    print(f'#{tc} ')

