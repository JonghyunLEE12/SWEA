n,m,k = map(int,input().split(' '))

parents = [ i for i in range(n+1)]
charges = [0] + list(map(int,input().split(' ')))


def find(target):
    if target == parents[target]:
        return target
    parents[target] = find(parents[target])
    return parents[target]



def union(a,b):
    a = find(a)
    b = find(b)

    if a != b:
        if charges[a] <= charges[b]:
            parents[b] = a
        else:
            parents[a] = b

for _ in range(m):
    v,w = map(int,input().split(' '))
    union(v,w)


ans = 0

for idx,root in enumerate(parents):
    if idx == root:
        ans += charges[idx]

if ans <= k:
    print(ans)

else:
    print('Oh no')