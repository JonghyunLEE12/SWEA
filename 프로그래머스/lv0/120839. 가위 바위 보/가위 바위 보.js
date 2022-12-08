function solution(rsp) {
    var answer = '';
    
    rsp = rsp.split("")
    
    for (let que of rsp) {
        if (que === '2') { answer += '0'}
        else if (que === '0') { answer += '5'}
        else if (que === '5') { answer += '2'}
    }
    return answer;
}