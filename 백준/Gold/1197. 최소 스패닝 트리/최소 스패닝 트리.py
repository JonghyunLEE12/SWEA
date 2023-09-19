'''
3 3
1 2 1
2 3 2
1 3 3
'''

v,e = map(int,input().split(' '))
parents = [ i for i in range(v+1)]

nodes = []
for _ in range(e):
    a,b,cost = map(int,input().split(' '))
    nodes.append([cost,a,b])

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

    if a != b:
        parents[max(a,b)] = min(a,b)
for cost,a,b in nodes:
    if find(a) != find(b):
        union(a,b)
        ans += cost

print(ans)