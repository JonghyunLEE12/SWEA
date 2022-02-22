import sys
from pprint import pprint

sys.stdin = open('input.txt')

def ant(arr):
    global p
    global q
    pprint(arr)
    p_plus = 1
    q_plus = 1
    while True:
        if t == 0:
            break
        # 개미 출발
        p += p_plus
        q += q_plus
        if p == w or p == h or q == w or q == h:
            if p == w :
                p_plus = -1
            if p == h :
                p
        break
    return

w,h = map(int,input().split())
p,q = map(int,input().split())
t = int(input())

matrix = [ [0 for _ in range(w+1)] for _ in range(h+1) ]
ant(matrix)