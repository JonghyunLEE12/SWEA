function solution(my_string) {
    var answer = '';
    const target = ['a','e','i','o','u']
    
    for ( let w of my_string) {
        if (target.includes(w)) { continue }
        answer += w
    }
    return answer;
}