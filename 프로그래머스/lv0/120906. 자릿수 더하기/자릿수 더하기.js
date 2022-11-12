function solution(n) {
    var answer = 0
    n = String(n).split("")
    for (let i of n) {
        answer += parseInt(i)
    }
    return answer;
}