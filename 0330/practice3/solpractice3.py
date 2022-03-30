import sys

sys.stdin = open('input.txt')

T = 1


def preorder(node):
    if node:
        print(node,end=' ')
        preorder(tree[node][0])
        preorder(tree[node][1])

def inorder(node):
    if node:
        inorder(tree[node][0])
        print(node,end=' ')
        inorder(tree[node][1])

def postorder(node):
    if node:
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node,end= ' ')

for tc in range(1, T + 1):
    n = int(input())
    numbers = list(map(int,input().split()))
    tree = [[0]*3 for _ in range(n+1)]

    for i in range(0,len(numbers)-1,2):
        parent_node = numbers[i]    # 부모
        child_node = numbers[i+1]   # 자식

        # 왼쪽 자식이 비어있다면 넣고
        if tree[parent_node][0] == 0:
            tree[parent_node][0] = child_node
        else:
            # 그렇지 않으면 오른쪽 자식에 넣자
            tree[parent_node][1] = child_node

        # 자식노드 부모 설정
        tree[child_node][2] = parent_node

    print(f'#{tc} ')

    print('== 전위 순회 ==')
    start_node = 1
    preorder(start_node)

    print()
    print('== 중위 순회 ==')
    inorder(start_node)

    print()
    print('== 후위 순회 == ')
    postorder(start_node)

