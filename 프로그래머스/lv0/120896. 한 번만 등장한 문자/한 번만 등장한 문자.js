function solution(s) {
    var answer = '';
    s = s.split("")
    
    let check = {}
    for ( let alpha of s) {
         check[alpha] = 0
    }
    
    for ( let alpha of s ) {
        check[alpha] += 1
    }
    
    for ( let alpha of s) {
        if ( check[alpha] === 1) { answer += alpha }
    }
    answer = answer.split("").sort().join("")
    return answer;
}