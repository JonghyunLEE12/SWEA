##부분 집합의 개수 중, 합이 0이 되는 거 찾기
import sys

sys.stdin = open('input.txt')

T = int(input())

def check(arr):
    n = len(arr)

    # 부분집합 구하기
    for i in range(1<<n):
        subs=[] # 부분 집합들을 담을 변수
        total = 0 # 합을 구할 total
        for j in range(n):
            if i & (1<<j):
                subs.append(arr[j])
        if len(subs) == 0: # 공집합인 경우
            continue
        else:
            for k in subs:
                total += k
            if total == 0: # 부분 집합의 합이 0이 되는 경우
                return 1
    return 0

for tc in range(1, T + 1):
    N = list(map(int,input().split()))
    print(f'#{tc} {check(N)}')

