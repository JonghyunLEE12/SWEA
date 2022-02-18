import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    rooms = [0]*400
    for i in range(N):
        x,y = map(int,input().split())
        if x < y:                       # x가 y보다 작은경우
            start = (x-1)//2            # 짝수방 , 홀수방
            end = (y-1)//2
        else :                          # x가 y보다 큰경우
            start = (y-1)//2
            end = (x-1)//2
        for j in range(start,end+1):
            rooms[j] += 1
    max_num = rooms[0]
    for num in rooms:
        if num > max_num:
            max_num = num
    print(f'#{tc} {max_num}')

