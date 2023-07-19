from collections import deque
def solution(n, roads, sources, destination):
    answer = []
    graph = dict()
    for i in range(1,n+1):
        graph[i] = []

    for a,b in roads:
        graph[a].append(b)
        graph[b].append(a)

    distance = [-1] * (n+1)

    q = deque()
    q.append([destination,0])
    visited = set()

    while q:
        v,l = q.popleft()
        if v in visited:
            continue
        visited.add(v)
        distance[v] = l

        for next in graph[v]:
            q.append([next,l+1])

    for s in sources:
        answer.append(distance[s])
    return answer