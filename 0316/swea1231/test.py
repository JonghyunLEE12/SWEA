import sys

sys.stdin = open('input.txt')

T = 10

# 중위순회
def inorder(v):
    if v > n:
        return
    if (v*2) <= n:
        inorder(v*2)
    print(node[v],end='')

    if (v*2+1) <= n:
        inorder(v*2+1)


for tc in range(1, T + 1):
    n = int(input())
    node = [0]*(n+1)                    # n+1 개로 이루어진 [0]개를 만든다.
    for i in range(n):
        matrix = list(input().split())
        node[int(matrix[0])] = matrix[1]    # 숫자번호대로 노드에 알파벳이 저장


    print(f'#{tc}',end=' ')
    inorder(1)
    print()