function solution(my_string) {
    var answer = 0;
    
    for (let w of my_string) {
        if (Number(w)) { answer += Number(w)}
    }
    return answer;
}