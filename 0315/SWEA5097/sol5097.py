import sys

sys.stdin = open('input.txt')

from collections import deque

T = int(input())


for tc in range(1, T + 1):
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    for _ in range(m):
        queue.append(queue.popleft())
    print(f'#{tc} {queue.popleft()}')
