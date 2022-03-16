import sys

sys.stdin = open('input.txt')

T = 10

def inorder(v):
    if v > n:
        return
    if (v*2) <= n:
        inorder(v*2)
    ans.append(node[v])

    if (v*2+1) <= n:
        inorder(v*2+1)

for tc in range(1, T + 1):
    n = int(input())
    node = [0] * (n+1)
    for i in range(n):
        vals = list(input().split())
        node[int(vals[0])] = vals[1]
    ans = []

    inorder(1)
    rlt = ''.join(ans)
    print(f'#{tc} {rlt}')

