import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    arr = input()
    cnt = 0
    sol = 0
    for i in range(len(arr)):
        if arr[i] == '(':
            cnt += 1
        else:
            cnt -= 1
            if arr[i-1] == 'C':
                sol += cnt
            else:
                sol +=1
    print(f'#{tc} {sol}')

