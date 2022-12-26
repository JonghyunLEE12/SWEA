function solution(id_list, report, k) {
    var answer = [];
    report = new Set(report)
    
    let singoDict = {}
    let reportDict = {}
    
    for (let id of id_list) {
        singoDict[id] = []
        reportDict[id] = 0
    }

    
    for (let rep of report) {
        rep = rep.split(' ')
        let name = rep[0]
        let re = rep[1]
        singoDict[name].push(re)
        reportDict[re] += 1
    }
    
    
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