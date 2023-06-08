'''
7 11
3 5
0 1 15
0 2 23
1 2 16
1 3 27
2 4 3
2 6 21
3 4 14
3 5 10
4 5 50
4 6 9
5 6 42
'''
import heapq

p,w = map(int,input().split(' '))
c,v = map(int,input().split(' '))

parents = [ x for x in range(p)]

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


pq = []
for _ in range(w):
    start,end,width = map(int,input().split(' '))
    heapq.heappush(pq, (-width,start,end))

while pq:
    cost,start,end = heapq.heappop(pq)
    cost = -cost
    union(start,end)

    if find(c) == find(v):
        result = cost
        break

print(result)


