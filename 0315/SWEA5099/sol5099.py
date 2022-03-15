import sys

sys.stdin = open('input.txt')
from collections import deque

T = int(input())


for tc in range(1, T + 1):
    n,m = map(int,input().split())
    pizza = deque(enumerate(map(int,input().split()),1))
    oven = deque()
    for i in range(n):
        oven.append(pizza.popleft())

    while len(oven) > 1:
        if len(oven) < n and pizza:
            oven.append(pizza.popleft())

        pizza_num , cheese = oven.popleft()

        if not cheese // 2:
            continue
        else:
            oven.append((pizza_num,cheese//2))

    print(f'#{tc} {oven.popleft()[0]}')

