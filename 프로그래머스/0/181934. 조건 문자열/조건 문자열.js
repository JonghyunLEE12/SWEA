function solution(ineq, eq, n, m) {
    var answer = 0;
    
    if (ineq == "<") {
        if (n <= m ) return 1
    }
    
    if (ineq == ">") {
     if (n > m ) return 1   
    }
    
    if (eq == "=") {
        if (n == m) return 1
    }
    return answer;
}
