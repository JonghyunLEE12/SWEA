from collections import deque
def solution(n, edge):
    answer = 0
    maps = [[] for _ in range(n + 1)]
    for i, j in edge:
        maps[i].append(j)
        maps[j].append(i)
    #간선 개수 최대 구하기
    node = [False] * (n + 1)
    node[1] = True
    dq = deque()
    dq.append((1,0))
    MAX = -2470000000 #최대 간선 개수
    while dq:
        now = dq.popleft()
        if MAX < now[1]:
            MAX = now[1]
        for nextNode in maps[now[0]]:
            if node[nextNode] == False:
                node[nextNode] = True
                dq.append((nextNode,now[1] + 1))
    #노드 개수 카운트
    node = [False] * (n + 1)
    node[1] = True            
    dq = deque()
    dq.append((1,0))
    while dq:
        now = dq.popleft()
        if MAX == now[1]:
            answer += 1
        for nextNode in maps[now[0]]:
            if node[nextNode] == False:
                node[nextNode] = True
                dq.append((nextNode,now[1] + 1))   
    return answer