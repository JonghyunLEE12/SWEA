import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    matrix = [[0]*10 for _ in range(10)]                # 0 으로 채워진 10x10 matrix 생성

    cnt = 0                                             # cnt 선언
    for i in range(N):
        r1,c1,r2,c2,color = map(int,input().split())    # 색칠해야할 범위와 색 입력 받음
        for a in range(r1,r2+1):                        # 범위 순회
            for b in range(c1,c2+1):
                if matrix[a][b] != 0:                   # 이미 색이 칠해진 곳이라면
                    matrix[a][b] = 3                    # 값을 3으로 변경
                    cnt += 1                            # cnt 값 증가
                else :
                    matrix[a][b] = color                # 색이 안칠하면 색을 칠하기
    print(f'#{tc} {cnt}')

