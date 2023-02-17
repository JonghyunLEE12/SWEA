# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y, number):
    number += str(graph[x][y])

    # 숫자 길이가 6이면 멈추고 똑같은 숫자의 합이 있는지 결과 리스트에서 확인
    if len(number) == 6:
        if number not in result:
            result.append(number)
        return

    # 좌/우/위/아래 방향의 좌표를 탐색
    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]

        # 맵 정보를 넘지 않는다면 탐색
        if 0 <= a < 5 and 0 <= b < 5:
            dfs(a, b, number)


# 2차원 맵 정보를 입력
graph = [list(map(int,input().split(' '))) for _ in range(5)]
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
result = []

for i in range(5):
    for j in range(5):
        dfs(i, j, "")

print(len(result))