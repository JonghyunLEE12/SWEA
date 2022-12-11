function solution(s) {
    var answer = 0;
    s = s.split(" ")
    let rlt = []
    for (let i of s) {
        if (i === 'Z') { rlt.pop() }
        else { rlt.push(Number(i)) }
    }
    answer = rlt.reduce((a,b) => a+b,0)
    return answer;
}