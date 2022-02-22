import sys

sys.stdin = open('input.txt')

T = int(input())

def dp(arr):
    dp = []
    start = 0
    energy = K
    while True:
        if start >= 10:
            break
        dp.append(start)
        now = start + K
        energy -= K
        if energy == 0:
            if arr[start] == 1:
                energy += K
                start = now
            else:
                for i in range(now, start , -1):
                    if arr[i] == 1:
                        energy += K
                        start = now
                else:
                    return 0

    return 1

for tc in range(1, T + 1):
    K,N,M = map(int,input().split())
    charge = list(map(int,input().split()))
    bus_stop = [0] * (N+1)
    for i in range(len(bus_stop)):
        if i in charge:
            bus_stop[i] += 1

    print(f'#{tc} {dp(bus_stop)}')

