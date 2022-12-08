function solution(my_string) {
    var answer = '';
    
    my_string = my_string.split("")
    
    for ( let s of my_string) {
        if ( s === s.toUpperCase()) { answer += s.toLowerCase()}
        else if (s === s.toLowerCase()) { answer += s.toUpperCase()}
    }
    return answer;
}