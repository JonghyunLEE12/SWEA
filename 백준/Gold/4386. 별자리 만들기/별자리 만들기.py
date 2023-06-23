
import math

n = int(input())
parents = [ x for x in range(n+1)]

stars = []

for i in range(n):
    x,y = map(float,input().split(' '))
    stars.append((x,y))

nodes = []

for i in range(n - 1):
    for j in range(i + 1, n):
        nodes.append((math.sqrt((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2), i, j))


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

nodes.sort()

ans = 0
for cost,a,b in nodes:
    if find(a) != find(b):
        union(a,b)
        ans += cost


print(round(ans,2))