function solution(k, score) {
    var answer = [];
    
    let rlt = []
    for (let sc of score ) {
        if (rlt.length < k) { 
            rlt.push(sc)
            rlt = rlt.sort((a,b) => a-b)
            answer.push(rlt[0])
        }
        else {
            rlt = rlt.sort((a,b) => a-b)
            if (sc > rlt[0]) {
                rlt.shift()
                rlt.unshift(sc)
            }
            rlt = rlt.sort((a,b) => a-b)
            answer.push(rlt[0])
        }
    }
    return answer;
}