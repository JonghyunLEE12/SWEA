import sys

sys.stdin = open('input.txt')

def BFS(start_node):
    visited[start_node] = 1
    Q.append(start_node)

    while Q:
        start_node = Q.pop(0)
        for next_node in range(1, N+1):
            if MyMap[start_node][next_node] and not visited[next_node]:
                visited[next_node] = 1
                Q.append(next_node)
                Distance[next_node] = Distance[start_node]+1

    return

TC = 10
for tc in range(1, TC+1):
    Len, init_num = map(int, input().split())
    Data = list(map(int, input().split()))
    N = max(Data)
    MyMap = [[0]*(N+1) for _ in range(N+1)]

    for i in range(Len//2):
        start = Data[i*2]
        end = Data[(i*2)+1]
        MyMap[start][end] = 1

    Q = []
    Distance, visited = [0]*(N+1), [0]*(N+1)

    BFS(init_num)

    max_D = Distance[0]
    for i in range(1, len(Distance)):
        if max_D <= Distance[i]:
            max_D = Distance[i]
            index = i
    print('#%s %d'%(tc, index))