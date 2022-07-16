def solution(lottos, win_nums):
    answer = []
    cnt = 0
    for i in lottos:
        if i in win_nums:
            cnt += 1
    cnt_0 = lottos.count(0)
    
    rank = {
        '6' : 1,
        '5' : 2,
        '4' : 3,
        '3' : 4,
        '2' : 5,
        '1' : 6,
        '0' : 6,
    }
    
    ans1 = str(cnt)
    ans2 = str(cnt+cnt_0)
    answer.append(rank[ans2])
    answer.append(rank[ans1])
 
    return answer