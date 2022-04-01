import sys

sys.stdin = open('input.txt')

n = int(input())
time = sorted(list(map(int,input().split())))
num = 0
for i in range(n):
    for j in range(i+1):
        num += time[j]
print(num)