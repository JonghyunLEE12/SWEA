import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    counter = [0]*1001
    for _ in range(N):
        bus_type , A, B = map(int,input().split())
        if bus_type == 1:
            for i in range(A,B+1):
                counter[i] += 1
        elif bus_type == 2:
            counter[A] += 1
            counter[B] += 1
            if A % 2:
                for j in range(A+1,B):
                    if j % 2:
                        counter[j] += 1
            else:
                for j in range(A+1,B):
                    if j%2 == 0:
                        counter[j] +=1
        elif bus_type == 3:
            counter[A] += 1
            counter[B] += 1
            if A % 2:
                for k in range(A+1,B):
                    if k % 3 == 0 and k % 10 != 0:
                        counter[k] +=1
            else:
                for k in range(A+1,B):
                    if k% 4 == 0:
                        counter[k] +=1
    max_v = 0
    for i in counter:
        if i > max_v:
            max_v = i
    print(f'#{tc} {max_v}')


