def solution(n, s):
    if n > s:
        return [-1]
    result = [s//n for _ in range(n)]
    sub = s % n
    for i in range(1, sub+1):
        result[-i] += 1
    return result