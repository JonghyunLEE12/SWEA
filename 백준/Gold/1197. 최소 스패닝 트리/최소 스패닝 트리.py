'''
3 3
1 2 1
2 3 2
1 3 3
'''

n,m = map(int,input().split(' '))

parents = [x for x in range(n+1)]

nodes = []
for _ in range(m):
    a,b,c = map(int,input().split(' '))
    nodes.append([c,a,b])

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
for cost,a,b in nodes:
    if find(a) != find(b):
        union(a,b)
        ans += cost

print(ans)