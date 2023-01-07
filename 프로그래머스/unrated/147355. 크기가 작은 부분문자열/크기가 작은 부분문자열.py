def solution(t, p):
    answer = 0

    for i in range(len(t)-len(p)+1):
        compare_num = t[i:i+len(p)]
        if int(compare_num) <= int(p):
            answer += 1
    return answer