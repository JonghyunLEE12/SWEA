def solution(n, words):
    answer = []
    used_words = []
    number , order = 0,0
    used_words.append((words[0]))
    lastword = words[0][-1]
    
    for i in range(1,len(words)):
        if words[i] not in used_words and words[i][0] == lastword:
            used_words.append(words[i])
            lastword = words[i][-1]
        else:
            number = (i//n)+1
            order = (i%n)+1
            break
            
    answer = [order ,number]
    return answer