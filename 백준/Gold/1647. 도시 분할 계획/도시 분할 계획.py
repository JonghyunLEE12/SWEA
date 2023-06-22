n,m = map(int,input().split(' '))
parents = [ x for x in range(n+1)]


def find(target):
    if target == parents[target]:
        return target
    else:
        y = find(parents[target])
        parents[target] = y
        return y


def union(a,b):
    a = find(a)
    b = find(b)

    if a != b:
        parents[a] = b

nodes = []

for _ in range(m):
    h,v,q = map(int,input().split(' '))
    nodes.append([q,h,v])

answer = 0
selected = []

nodes.sort()
for cost,a,b in nodes:
    if find(a) != find(b):
        union(a,b)
        answer += cost
        selected.append(cost)

answer -= selected.pop()
print(answer)