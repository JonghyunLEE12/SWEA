import sys

sys.stdin = open('input.txt')

T = int(input())

def check(N):
    memo = [1,3]                                    # n = 1 일때 : 1 , n = 2 일때 : 3
    for i in range(2, N//10):                       # 1->1 ,2->3 ,3->5 ,4->11
        memo.append(memo[i-1] + ( 2 * memo[i-2] ))  # 규칙 : memo[i-1] + ( 2 * memo[i-2] ))
    return memo
for tc in range(1, T + 1):
    N = int(input())
    memo = check(N)
    max_memo = memo[0]
    for i in memo:
        if i > max_memo:
            max_memo = i
    print(f'#{tc} {max_memo}')

