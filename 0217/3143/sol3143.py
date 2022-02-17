import sys

sys.stdin = open('input.txt')

def counter(A,B):
    cnt = 0
    idx = 0
    while True:
        if idx >= len(A):               # 인덱스가 A보다 크거나 같아질때 종료
            break
        if A[idx:idx+len(B)] == B:      # A[idx 부터 idx+B 의 길이] 만큼 출력한결과가 B와 같을 때,
            cnt += 1                    # cnt 증가
            idx += len(B)               # 같은 걸 확인 했을 때에는 인덱스를 B의 길이만큼 증가
        else:                           # 아닐 때에는, cnt 1 증가, 인덱스 1 증가하여 다음 문자를 살펴봄
            cnt += 1
            idx += 1
    return cnt

T = int(input())
for tc in range(1, T + 1):
    A,B = input().split()
    cnt=counter(A,B)
    print(f'#{tc} {cnt}')

