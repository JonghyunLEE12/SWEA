def longest_palindrome(s, left, right):
    if right - left == 1:
        length = 0
    else:
        length = 1
        
    while left >= 0 and right < len(s):
        if s[left] == s[right]:
            left -= 1
            right += 1
            length += 2
        else:
            break
            
    return length


def solution(s):
    answer = 1
    
    if len(s) == 1 or s == s[::-1]:
        return len(s)
    
    for i in range(len(s)-1):
        answer = max(answer, longest_palindrome(s, i, i+1), longest_palindrome(s, i, i+2) )
        
    return answer