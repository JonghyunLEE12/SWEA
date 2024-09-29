def solution(id_list, report, k):
    answer = []
    report = set(report)
    singo_dic = dict()
    report_dic = dict()
    
    for id in id_list:
        singo_dic[id] = []
        report_dic[id] = 0
    
    for rep in report:
        name,report = rep.split( )
        singo_dic[name].append(report)
        report_dic[report] += 1
    
            
    for id in id_list:
        cnt = 0
        for singo in singo_dic[id]:
            if report_dic[singo] >= k:
                cnt += 1
        answer.append(cnt)
    
        
    return answer