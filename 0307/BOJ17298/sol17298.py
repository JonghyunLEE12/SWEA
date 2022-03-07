import sys

sys.stdin = open('input.txt')




N = int(input())
matrix = list(map(int,input().split()))
NGE = [-1]*N
stack = []

for idx in range(len(matrix)):
    while stack and matrix[stack[-1]] < matrix[idx]:
        NGE[stack.pop()] = matrix[idx]
    stack.append(idx)

print(*NGE)


