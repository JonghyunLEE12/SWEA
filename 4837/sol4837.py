import sys

sys.stdin = open('input.txt')

T = int(input())

def subs(lst):
    # A의 부분집합 만들기
    sub = [[]]                              # 공집합 포함 리스트 sub 선언
    for i in lst:
        for j in range(len(sub)):
            sub.append(sub[j]+[i])          # A의 부분집합을 만든다.
    return sub

def check(sub):
    global N
    global K
    cnt = 0
    for num in sub:                         # num 이 sub를 순회 하면서
        sum_num = 0                         
        if len(num) == N:                   # num 이 N개의 원소를 가지고 있다면
            for i in num:                   # i가 num을 순회
                sum_num += i                # sum_num을 더함
            if sum_num == K:                # sum_num == K 일때,
                cnt += 1                    # cnt 증가
    return cnt

for tc in range(1, T + 1):
    N , K = map(int,input().split())
    A = [i for i in range(1,13)]
    sub = subs(A)
    print(f'#{tc} {check(sub)}')

