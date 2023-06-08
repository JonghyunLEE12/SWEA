def solution(genres, plays):
    answer = []
    
    music = dict()
    
    for idx,genre in enumerate(genres):
        music[idx] = [genre]
    
    
    for idx,time in enumerate(plays):
        music[idx].append(time)
    
    
    
    total = {}
    
    for value in music.values():
        total[value[0]] = 0
    
    for value in music.values():
        total[value[0]] += value[1]
    
    total = list(total.items())
    total.sort(key = lambda x:x[1] , reverse = True)
    
    rlt_dict = {}
    
    for i in total:
        rlt_dict[i[0]] = []
    
    
    for k,v in music.items():
        rlt_dict[v[0]].append([k,v[1]])

        
    for k,v in rlt_dict.items():
        v.sort(key = lambda x:x[1],reverse = True)
    

    def ans(k,v):
        lst = []
        for i in v:
            if len(lst) == 2:
                break
            lst.append(i[0])
            
        for j in lst:
            answer.append(j)
    
    for k,v in rlt_dict.items():
        ans(k,v)
        

    return answer