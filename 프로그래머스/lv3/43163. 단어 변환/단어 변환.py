from collections import deque

def solution(begin, target, words):
    queue = deque()
    length = len(words)
    word_length = len(begin)
    
    def check(word,change):
        diff = 0
        for i in range(word_length):
            if word[i] != change[i]:
                diff += 1
        if diff == 1:
            return True
        else:
            return False
    
    def bfs():
        queue.append([begin,0])            # 0 => depth
        
        if target not in words:
            return 0
        
        while queue:
            word , depth = queue.popleft()
            for change in words:
                if check(word , change):
                    if change == target:
                        return depth + 1
                    else:
                        queue.append([change,depth+1])
    
    answer = bfs()
    return answer