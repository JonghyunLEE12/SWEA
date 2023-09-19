# 유니온 파인드
import sys



def union(x, y):
    parent[find(y)] = find(x)


# 경로압축 포함한 find 함수
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]


n,m = map(int,input().split())
parent = [x for x in range(n+1)]

for _ in range(m):
    o,a,b = map(int,sys.stdin.readline().split())
    if o == 0:
        union(a,b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
