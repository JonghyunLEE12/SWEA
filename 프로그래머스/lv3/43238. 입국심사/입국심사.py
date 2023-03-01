def solution(n, times):
    answer = 0
    
    # right => 가장 비효율적으로 심사 했을 때 걸리는 시간
    # 가장 긴 심사시간 : 심사관 n 명에게 모두 심사받는 경우
    
    left, right =  1, max(times)*n
    while left <= right:
        mid = (left + right) // 2
        people = 0
        for time in times:
            people += mid // time
            if people >= n:
                break
        
        
        if people >= n:
            answer = mid
            right = mid - 1
        
        elif people < n :
            left = mid + 1
    
    
    return answer