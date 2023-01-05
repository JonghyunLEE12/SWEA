def dfs(player,score):
    global max_score
    
    if player == 11:
        max_score = max(max_score,score)
        return

    for i in range(11):
        if visited[i] or not matrix[player][i]:
            continue
        visited[i] = 1
        dfs(player+1,score+matrix[player][i])
        visited[i] = 0

C = int(input())
for _ in range(C):
    matrix = [list(map(int,input().split(' '))) for _ in range(11)]
    visited = [0] * 11
    max_score = 0
    dfs(0,0)
    print(max_score)