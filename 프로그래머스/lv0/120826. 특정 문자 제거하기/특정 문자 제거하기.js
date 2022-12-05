function solution(my_string, letter) {
    var answer = '';
    my_string = my_string.split("")
    for (let w of my_string) {
        if ( w === letter) { continue }
        answer += w
    }
    return answer;
}