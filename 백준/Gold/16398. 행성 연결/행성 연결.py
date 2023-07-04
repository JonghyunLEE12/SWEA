'''
5
0 6 8 1 3
6 0 5 7 3
8 5 0 9 4
1 7 9 0 6
3 3 4 6 0
'''

n = int(input())

parents = [ x for x in range(n+1)]
graph =  [ list(map(int,input().split(' '))) for _ in range(n)]
nodes = []

for a in range(n):
    for b in range(a+1,n):
        nodes.append((graph[a][b],a,b))

nodes.sort()


ans = 0

def find(t):
    if t == parents[t]:
        return t
    else:
        y = find(parents[t])
        parents[t] = y
        return y

        
def union(a,b):
    a = find(a)
    b = find(b)

    if a > b:
        parents[a] = b
    else:
        parents[b] = a
for node in nodes:
    cost,a,b = node

    if find(a) != find(b):
        union(a,b)
        ans += cost


print(ans)