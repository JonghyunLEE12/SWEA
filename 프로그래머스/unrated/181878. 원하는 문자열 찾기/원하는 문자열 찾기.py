def solution(myString, pat):
    answer = 0
    
    myString = myString.lower()
    pat = pat.lower()
    
    if pat in myString:
        return 1
    return answer