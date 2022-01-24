#baekjoon1110
from turtle import numinput


N = int(input())

number = N
cnt = 0
while True:
    a = number //10
    b = number % 10
    c = (a+b) % 10
    number = (b*10) + c
    cnt += 1
    if number == N:
        break
print(cnt)