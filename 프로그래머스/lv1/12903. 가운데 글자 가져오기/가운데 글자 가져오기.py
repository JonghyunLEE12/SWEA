def solution(s):
    answer = ''
    if len(s) % 2:
        answer = s[int(len(s)/2)]
    else:
        middle = int(len(s)/2)
        answer = s[middle-1] + s[middle]
    return answer