def solution(my_str, n):
    answer = []
    my_str = list(my_str)
    
    n_word = ''
    for alpha in my_str:
        n_word += alpha
        if len(n_word) == n:
            answer.append(n_word)
            n_word = ''
        
    answer.append(n_word)
    if len(answer[-1]) == 0:
        answer.pop()
    return answer