import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    num = int(input())
    numbers = list(map(int,input().split()))
    numbers = numbers[::-1]                     # 역순으로 돌려준다.
    max_num = numbers[0]                        # 최대값은 리스트의 첫번째값
    rlt = 0                                     # 결과를 담아줄 변수
    for i in range(1,len(numbers)):             # i 가 순회 ( max_num을 인덱스 0 번째 값 부터 지정해줘서 1부터 시작 )
        if max_num > numbers[i]:                # max_num 이 numbers[i] 보다 큰 경우
            rlt += max_num - numbers[i]         # 결과에 max_num - numbers 저장
        else :
            max_num = numbers[i]                # 반대의 경우 max_num 갱신
    print(f'#{tc} {rlt}')