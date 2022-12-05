function solution(s1, s2) {
    var answer = 0;
    
    for ( let i of s1) {
        for (let j of s2) {
            if ( i === j) { answer += 1}
        }
    }
    return answer;
}