import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    bus_stop = [0]* 5001                        # 왜 5000이면 에러가 날까요?
    for i in range(N):
        A , B = map(int,input().split())        # A , B 입력

        for j in range(A,B+1):
            bus_stop[j] += 1                    # i가 순회하면서 정류장 값에 1증가

    P = int(input())

    print(f'#{tc}',end=' ')
    for k in range(P):
        check = int(input())
        print(bus_stop[check],end =' ')         # 정류장 지나간 버스 수 출력
    print()



