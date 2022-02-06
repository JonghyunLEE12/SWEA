import copy
# 90도 회전 함수 선언
def turn_90(lst): 
    # 결과 리스트를 깊은 복사
    rlt_lst = copy.deepcopy(lst)
    # x 좌표 :0
    x = 0
    # y 좌표 : lst길이 -1
    y = len(lst) - 1
    while True:
        # 결과 리스트에 90도 회전한 값을 저장
        for i in range(0,len(lst)):
            rlt_lst[i][y] = lst[x][i]
        # y 가 0이 될때 까지 반복
        if y == 0:
            break
        x += 1
        y -= 1
    return rlt_lst


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = []
    # 리스트 값 저장
    for i in range(N):
        lst.append(list(map(int,input().split())))

    print(f'#{tc}')
    for i in range(N):
        # 90도 회전한 값 출력
        for a in range(N):
            print(turn_90(lst)[i][a], end='')
        print(end=' ')
        # 180도 회전한 값 출력
        for b in range(N):
            print(turn_90(turn_90(lst))[i][b], end='')
        print(end=' ')
        # 270도 회전한 값 출력
        for c in range(N):
            print(turn_90(turn_90(turn_90(lst)))[i][c], end='')
        print(end=' ')
        print()