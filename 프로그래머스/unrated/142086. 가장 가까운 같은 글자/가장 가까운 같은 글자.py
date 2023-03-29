def solution(s):
    answer = []
    for i in range(len(s)):                #해당 문자열 길이만 큼 반복
        if s[i] in s[:i]:                  #해당 문자가 현재 인덱스까지의 문자열에 존재한다면
            while s[:i].count(s[i])>1:     #현재 인덱스까지의 문자열내에 여러개 존재한다면 1개가 남을때까지 반복
                s = s.replace(s[i],'0',1)  #해당 문자 replace
            answer.append(i-s.index(s[i])) #가까운 해당 문자의 길이 출력
        else:                              #해당 문자가 현재 인덱스까지의 문자열에 존재하지 않는다면
            answer.append(-1)              #-1 출력
    return answer