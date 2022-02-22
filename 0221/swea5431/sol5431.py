import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N , K = map(int,input().split())
    stu = [ num for num in range(1,N+1)]
    submit_lst = list(map(int,input().split()))

    bad_stu = []
    for s in stu:
        if s in submit_lst:
            continue
        else:
            bad_stu.append(s)
    print(f'#{tc}',end=' ')
    print(*bad_stu)

