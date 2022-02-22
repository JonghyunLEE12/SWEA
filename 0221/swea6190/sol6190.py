import sys

sys.stdin = open('input.txt')

T = int(input())

def check(num):
    num = str(num)
    for i in range(len(num)-1):
        if num[i] > num[i+1]:
            return False
    return True

def rlt(arr):
    max_num = -1                        # 단조 증가 하는 수가 없으면 -1
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            num = arr[i]*arr[j]
            if num > max_num and check(num):
                max_num = num
    return max_num


for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int,input().split()))
    print(f'#{tc} {rlt(arr)}')