import sys

sys.stdin = open('input.txt')

T = int(input())

def sol(switch,want):
    cnt = 0
    for i in range(1,N+1):
        if switch[i] == want[i]:
            continue
        else:    # 다르네
            cnt += 1
            # i의 배수만큼 스위치를 켜라
            for j in range(1,len(switch)):
                if j % i == 0:
                    if switch[j] == 1:
                        switch[j] = 0
                    elif switch[j] == 0:
                        switch[j] = 1
        if switch == want:
            return cnt
    return cnt
for tc in range(1, T + 1):
    N = int(input())
    switch = [0]+[0]*N
    want_pattern = [0]+list(map(int,input().split()))
    ans = sol(switch,want_pattern)
    print(f'#{tc} {ans}')

