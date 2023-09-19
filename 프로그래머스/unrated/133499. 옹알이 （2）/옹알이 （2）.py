def solution(babbling):
    ans = 0
    
    baby = ['aya','ye','woo','ma']
    
    rlt = []
    
    def dfs(target,prev_word):
        if len(target) == 0:
            return 1
        
        count = 0
        for sound in baby:
            if target.startswith(sound) and prev_word != sound:
                count += dfs(target[len(sound):],sound)
        return count
    
    for target in babbling:
        rlt.append(dfs(target,""))
                
    return sum(rlt)

