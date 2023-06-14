'''
6
9
1 2 5
1 3 4
2 3 2
2 4 7
3 4 6
3 5 11
4 5 3
4 6 8
5 6 8
'''

n = int(input())
m = int(input())

parents = [ x for x in range(n+1)]
costs = [ 0 for _ in range(n+1)]

def find(target):
    if parents[target] == target:
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

q = []

for _ in range(m):
    h,v,cost = map(int,input().split(' '))
    q.append([cost,h,v])

q.sort(key =lambda x: x[0])


ans = 0
for cos,a,b in q:
    if find(a) != find(b):
        union(a,b)
        ans += cos

print(ans)
    