// def solution(id_list, report, k):
//     answer = []
//     report = set(report)
//     singo_dic = dict()
//     report_dic = dict()
    
//     for id in id_list:
//         singo_dic[id] = []
//         report_dic[id] = 0
    
//     for rep in report:
//         name,report = rep.split( )
//         singo_dic[name].append(report)
//         report_dic[report] += 1
    
            
//     for id in id_list:
//         cnt = 0
//         for singo in singo_dic[id]:
//             if report_dic[singo] >= k:
//                 cnt += 1
//         answer.append(cnt)
    
        
//     return answer

function solution(id_list, report, k) {
    var answer = [];
    report = new Set(report)
    
    let singoDict = {}
    let reportDict = {}
    
    for (let id of id_list) {
        singoDict[id] = []
        reportDict[id] = 0
    }
//     for rep in report:
//         name,report = rep.split( )
//         singo_dic[name].append(report)
//         report_dic[report] += 1
    
    for (let rep of report) {
        rep = rep.split(' ')
        let name = rep[0]
        let re = rep[1]
        singoDict[name].push(re)
        reportDict[re] += 1
    }
    
    //     for id in id_list:
//         cnt = 0
//         for singo in singo_dic[id]:
//             if report_dic[singo] >= k:
//                 cnt += 1
//         answer.append(cnt)
    
    for (let id of id_list) {
        let cnt = 0
        for (let singo of singoDict[id]) {
            if (reportDict[singo] >= k){
                cnt += 1
            }
        }
        answer.push(cnt)
        
        
    }
    
    
    
    return answer;
}