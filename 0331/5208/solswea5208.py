import sys

sys.stdin = open('input.txt')

T = int(input())

def recur(now,cnt):
    global rlt

    if now == n-1:
        rlt = min(rlt,cnt)
        return

    if rlt <= cnt:
        return

    for i in range(1,lst[now]+1):
        recur(now+i,cnt+1)

for tc in range(1, T + 1):
    lst = list(map(int,input().split()))
    n = lst.pop(0)
    rlt = float('inf')
    recur(0,0)
    print(f'#{tc} {rlt}')

