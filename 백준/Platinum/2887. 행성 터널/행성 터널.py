'''
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19
'''

n = int(input())
parents = [ x for x in range(n+1) ]


xlst,ylst,zlst = [],[],[]

for i in range(n):
    x,y,z = map(int,input().split(' '))
    xlst.append((x,i))
    ylst.append((y,i))
    zlst.append((z,i))


xlst.sort()
ylst.sort()
zlst.sort()

nodes = []


for curlist in xlst,ylst,zlst:
    for i in range(1,n):
        n1,a = curlist[i-1]
        n2,b = curlist[i]

        nodes.append((abs(n1-n2),a,b))
    
nodes.sort()

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

ans = 0

for cost,a,b in nodes:

    if find(a) != find(b):
        union(a,b)
        ans += cost

print(ans)