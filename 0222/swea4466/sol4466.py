import sys

sys.stdin = open('input.txt')

T = int(input())

def sol(arr):
    max_lst = []
    for i in range(K):
        max_num = max(arr)
        max_lst.append(max_num)
        arr.remove(max_num)
    return max_lst

for tc in range(1, T + 1):
    N , K = map(int,input().split())
    scores = list(map(int,input().split()))
    rlt = sol(scores)
    print(f'#{tc} {sum(rlt)}')

