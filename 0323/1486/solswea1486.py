import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    n,b = map(int,input().split())
    crew = list(map(int,input().split()))

    # 높이가 B 이상인 탑 중에서 탑의 높이와 B의 차이가 가장 낮은것을 출력
    # 탑 직원이 한명이면 - > 한사람이고 두사람이면 -> 두사람의 합

    subset = [[]]
    for i in crew:
        for j in range(len(subset)):
            subset.append(subset[j]+[i])

    min_num = 1000000000
    rlt = 0
    for i in subset:
        if sum(i) > b:
            rlt = sum(i) - b
            if rlt < min_num:
                min_num = rlt
    print(f'#{tc} {min_num}')

