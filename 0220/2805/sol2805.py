import sys

sys.stdin = open('input.txt')

T = int(input())

def farm(arr):
    middle = len(arr)//2
    start = middle
    end = middle
    sum_num = 0
    for i in range(len(arr)):
        for j in range(start,end+1):
            sum_num += int(arr[i][j])
        if i < middle:
            start -= 1
            end +=1
        else:
            start += 1
            end -= 1
    return sum_num

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(input()) for _ in range(N)]
    print(f'#{tc} {farm(matrix)}')

